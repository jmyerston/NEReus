# NEReus

#  A Named Entity Corpus of Ancient Greek



NEReus is an annotated corpus of ancient Greek Named Entities and Non Named Entities developed to train neural models. The corpus is in beta stage.  The project aims to provide NER annotations of the following text in ancient Greek:

* Hesiod 
	- [ ] *Theogony*

* Herodotus' *Histories*

  - [x] Book I

  - [ ] Book II
  - [x] Book III
* Diogenes  Laertius' *Lives of Eminent Philosophers*

  * [x] Book I
  * [x] Book III
  * [x] Book IV
* Euripides
  * [x] *Bacchae*
* Apollodorus' Library
  * [ ] Book I
* [ ] Selected passages from Pausanias' *Description of Greece*
* [ ]  Selected passages from Strabo's *Geography*

## Schema

The annotation schema of NEReus (v2) consists of four labels: **PERSON, GOD, LOC, ETHNO**.

An earlier version of the schema also had **NORP** and **LANGUAGE** as separate labels: NORP was renamed to ETHNO with narrowed scope (see below), and LANGUAGE was dropped as an NER label entirely — language/dialect terms are now handled by a separate rule-based component instead of the neural NER model. LOC briefly split into LOC and GEO (political places vs. natural features), then the two were merged back into one LOC.

### PERSON

Named individual human beings, mortal or heroic — Θαλῆς, Κροῖσος, Ἡρόδοτος, Ἀχιλλεύς, Ὀδυσσεύς. The Pythia (ἡ Πυθία) is annotated as PERSON, treating the institutional role as an individual. Ἡρακλῆς is context-dependent: PERSON when he acts as the protagonist of heroic narrative (his labors, his death), GOD when he appears in theological, cultic, or comparative-religion discourse, or is equated with a foreign god.

Substantivized ethnonyms (ὁ Φοῖνιξ, "the Phoenician [man]") are **not** labeled PERSON, even when they refer to one specific individual in context — they stay ETHNO (see below). This reverses the rule from the earlier schema version.

### GOD

In contrast to most modern NER schemas, NEReus annotates the names of gods and other supernatural beings. This is so because people in the ancient world perceived many divine beings as real things to which they related in various forms — a critical form of relating to the gods was kinship, as some individuals imagined they had divine ancestry.

This includes the Olympian gods (Ζεύς, Ἥρα, Ἀθηνᾶ, Ἀπόλλων, Ἄρτεμις, Ἑρμῆς, Ἀφροδίτη, Διόνυσος, ...), Titans and primordial beings (Κρόνος, Ῥέα, Γαῖα, Οὐρανός, ...), personified abstractions (Δίκη, Νέμεσις, Μοῖραι, Χάριτες, ...), and supernatural races (Τιτᾶνες, Κύκλωπες, Γίγαντες, Κένταυροι) — these last four are always GOD, never ETHNO, even though a passage may describe them collectively the way it would a human people. Διόνυσος is always GOD, regardless of how mortal or theatrical his appearance is in a given narrative (e.g. in Euripides' *Bacchae*), since he retains full divine cult status throughout.

### LOC

All named places: cities, kingdoms, empires, islands, regions, and continents (Θῆβαι, Κρήτη, Περσία, Λιβύη, Εὐρώπη), as well as natural geographical features and mythological places (Ὄλυμπος, Νεῖλος, Εὔξεινος, Τάρταρος). A single LOC label now covers both — an earlier version of the schema split these into LOC (political places) and GEO (natural features), but the distinction was dropped because it added recurring, hard-to-adjudicate judgment calls (place names like Σκυθίη or Θράκη oscillate between a political and a purely geographical sense depending on context) without a matching benefit.

When an adjective and a generic geographic noun together name one specific place (a sea, mountain, river, lake, or region), the whole phrase is annotated as a single LOC span rather than stripping the adjective as an epithet — e.g. Ἐρυθρὴ θάλασσα ("the Red Sea"), Καυκάσιον ὄρος ("Mount Caucasus"), Ξάνθιον πεδίον ("the Xanthian plain"). The generic noun is the head of the name, not a modifying epithet.

### ETHNO

Human ethnic, national, and tribal groups — Ἕλληνες, Πέρσαι, Σκύθαι, Αἰγύπτιοι, Λυδοί, Φοίνικες. This label absorbs what the earlier schema called NORP, but with narrower scope:

* Substantivized singular ethnonyms (ὁ Φοῖνιξ, ὁ Μῆδος) remain ETHNO even when they refer to one specific individual in context — they are never relabeled PERSON. An appositive construction like Μαζάρης ὁ Μῆδος ("Mazares the Mede") is annotated as **two separate spans**: PERSON (Μαζάρης) and ETHNO (Μῆδος), not merged into one.
* ETHNO excludes philosophical schools, religious organizations, and other non-ethnic social or professional groups — Στωικοί ("Stoics") or Ἐπικούρειοι ("Epicureans") are not annotated as ETHNO.
* ETHNO excludes the supernatural races that fall under GOD — Τιτᾶνες, Κύκλωπες, Γίγαντες, and Κένταυροι are never ETHNO, even in contexts that describe them collectively as a people.

### Span rules

* The definite article is never included in an annotated span, regardless of label.
* Punctuation, conjunctions, and prepositions are never included at a span's edges.
* Attributive epithets and modifying adjectives are excluded from PERSON and GOD spans — only the core name is annotated (e.g. "Ποσειδάωνα γεήοχον" → the GOD span is "Ποσειδάωνα" only). The one exception is the LOC adjective-plus-generic-noun compound described above.

## Non-Named Entities

For literary studies Named Entitiy Recognition is not enough as researchers may want to explore which animals, smells, and emotions are associated with cerain places and peoples. So, in the feature I plan to add annotation of non-named entities to the dataset. 

## License

The underlying ancient Greek texts are drawn from the [Perseus Digital Library](http://www.perseus.tufts.edu/) (Perseus Project, Tufts University), via the [Perseus canonical-greekLit](https://github.com/PerseusDL/canonical-greekLit) repository, which licenses its texts under a Creative Commons Attribution-ShareAlike 4.0 International License. In keeping with that license's ShareAlike term, NEReus — the source text together with its named-entity annotations — is released under the same license:

**[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)**

See the [LICENSE](LICENSE) file for the full terms and source-text attribution. In short: you're free to share and adapt this corpus, including commercially, as long as you credit Perseus Digital Library and the NEReus project and release any derivative work under the same license.



 
