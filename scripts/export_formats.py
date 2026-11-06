"""Write the .ner and _hf.jsonl formats of the corpus from its .jsonl files.

    python scripts/export_formats.py [FILE.jsonl ...]

Without files it exports corpus/nereus_train.jsonl and corpus/nereus_dev.jsonl. Each FILE.jsonl
gives two files next to it:

* FILE.ner: one `token<TAB>BILUO tag` per line, with a blank line after each sentence;
* FILE_hf.jsonl: one {"id", "tokens", "ner_tags", "meta"} per line, with BILUO tags.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_FILES = [ROOT / "corpus" / "nereus_train.jsonl", ROOT / "corpus" / "nereus_dev.jsonl"]


def biluo_tags(example: dict) -> list[str]:
    tags = ["O"] * len(example["tokens"])
    for span in example["spans"]:
        first, last, label = span["token_start"], span["token_end"], span["label"]
        if first == last:
            tags[first] = f"U-{label}"
        else:
            tags[first] = f"B-{label}"
            for index in range(first + 1, last):
                tags[index] = f"I-{label}"
            tags[last] = f"L-{label}"
    return tags


def export(path: Path) -> None:
    ner_lines = []
    hf_lines = []
    examples = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    for index, example in enumerate(examples):
        words = [token["text"] for token in example["tokens"]]
        tags = biluo_tags(example)
        ner_lines += [f"{word}\t{tag}\n" for word, tag in zip(words, tags)] + ["\n"]
        record = {"id": str(index), "tokens": words, "ner_tags": tags, "meta": example["meta"]}
        hf_lines.append(json.dumps(record, ensure_ascii=False) + "\n")
    path.with_suffix(".ner").write_text("".join(ner_lines), encoding="utf-8")
    path.with_name(f"{path.stem}_hf.jsonl").write_text("".join(hf_lines), encoding="utf-8")
    print(f"{path.name}: exported {len(examples)} sentences")


if __name__ == "__main__":
    for file in [Path(arg) for arg in sys.argv[1:]] or DEFAULT_FILES:
        export(file)
