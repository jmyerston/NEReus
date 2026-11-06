"""Correct typos of the source editions in the .jsonl corpus, using a list of whole tokens.

    python scripts/fix_typos.py [--csv scripts/typos.csv] [--dry-run] [FILE.jsonl ...]

Without files it corrects corpus/nereus_train.jsonl and corpus/nereus_dev.jsonl in place.

The CSV has the columns typo, correction and note. A row applies only to tokens equal to `typo`,
so that a mark like » stays where it is a quotation mark. An empty correction deletes the token.
Token offsets and spans are computed again, and lines without typos are kept byte for byte. A
span that would lose all of its tokens is an error, and no file is written.
"""
import argparse
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILES = [ROOT / "corpus" / "nereus_train.jsonl", ROOT / "corpus" / "nereus_dev.jsonl"]


def read_typos(path: Path) -> dict[str, str]:
    typos: dict[str, str] = {}
    with open(path, encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            typo = row["typo"].strip()
            if not typo:
                raise ValueError(f"{path}: a row has no typo: {row}")
            if typo in typos:
                raise ValueError(f"{path}: repeated typo {typo}")
            typos[typo] = row["correction"].strip()
    return typos


def correct(example: dict, typos: dict[str, str], counts: Counter) -> dict:
    words: list[tuple[str, bool]] = []
    new_index: list[int | None] = []
    for token in example["tokens"]:
        text = token["text"]
        if text in typos:
            counts[text] += 1
            text = typos[text]
        if text:
            new_index.append(len(words))
            words.append((text, token["ws"]))
        else:  # the token is deleted: the previous token takes over its space
            new_index.append(None)
            if words and token["ws"]:
                words[-1] = (words[-1][0], True)

    tokens = []
    position = 0
    for index, (text, space) in enumerate(words):
        tokens.append({"text": text, "start": position, "end": position + len(text), "id": index, "ws": space})
        position += len(text) + (1 if space else 0)
    full_text = "".join(t["text"] + (" " if t["ws"] else "") for t in tokens)
    if not example["text"].endswith(" "):
        full_text = full_text.rstrip(" ")

    spans = []
    for span in example["spans"]:
        kept = [new_index[i] for i in range(span["token_start"], span["token_end"] + 1) if new_index[i] is not None]
        if not kept:
            raise ValueError(f"the span {span} would lose all of its tokens: {example['text'][:60]}")
        first, last = tokens[kept[0]], tokens[kept[-1]]
        spans.append({**span, "start": first["start"], "end": last["end"], "token_start": first["id"], "token_end": last["id"]})
    return {**example, "text": full_text, "tokens": tokens, "spans": spans}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", type=Path, default=DEFAULT_FILES)
    parser.add_argument("--csv", type=Path, default=Path(__file__).with_name("typos.csv"))
    parser.add_argument("--dry-run", action="store_true", help="report the corrections without writing")
    args = parser.parse_args()

    typos = read_typos(args.csv)
    counts: Counter = Counter()
    outputs: dict[Path, list[str]] = {}
    for path in args.files:
        lines = []
        for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
            example = json.loads(line)
            if any(token["text"] in typos for token in example["tokens"]):
                line = json.dumps(correct(example, typos, counts), ensure_ascii=False) + "\n"
            lines.append(line)
        outputs[path] = lines

    if not args.dry_run:
        for path, lines in outputs.items():
            path.write_text("".join(lines), encoding="utf-8")
    for typo, correction in typos.items():
        print(f"{counts[typo]:4}  {typo} -> {correction or '(deleted)'}")
    missing = [typo for typo in typos if not counts[typo]]
    if missing:
        print(f"{len(missing)} typos not found (already corrected?)")


if __name__ == "__main__":
    main()
