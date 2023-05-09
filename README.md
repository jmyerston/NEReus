# NEReus

#  A Named Entity Corpus of Ancient Greek



NEReus is an annotated corpus of Named Entities in ancient Greek text, developed for the training of neural models. At this point the corpus is an alpha stage and consist only of the annotated version of Herodotus's Histories Book III, which has been revised and has reached the golden standard landmark.  The project aims to to provide NER annotations of the following text in ancient Greek:

- [x] Hesiod's *Theogony*

* Herodotus' *Histories*

  - [ ] Book I

  - [ ] Book II
  - [x] Book III

* Diogenes  Laertius' *Lives of Eminent Philosophers*

  * [ ] Book I
  * [ ] Book III
  * [ ] Book V
  * [ ] Book  VII

* [ ] Selected passages from Pausanias' *Description of Greece*

* [ ]  Selected passages from Strabo's *Geography*

## Schema

The annotation schema of NEReus consists of the labels **NORP, GOD, GPE, LANGUAGE, LOC, PERSON** whose description is the following:

### NORP

The label **NORP**  refers to adjective which denote:

* Ethnic groups like Greeks, Egyptians, Persians, etc.  **NORP** contains then *ethnonyms* both in the singular and in the plural.
* *Demonyms*, this is, terms used to denote the natives or inhabitants of a particular city, city-state, or sub-division of a city-state like the *demos* or *tribes* are also labeled as **NORP**   
* Other types of social groups, like philosophical schools, religious organizations like *thiasos*, temple personnel, groups of doctors, and similar are also labeled as **NORP** .
* **<u>Exceptions</u>** are substantivized adjectives in the singular that function as a proper noun like in "the Phoenician". Such cases are labeled as **PERSON** , including the article as in ὁ Φοῖνιξ.

### GOD

In contrast to  modern NER corpora, **NEReus** annotates the names of gods and other supernatural beings. This is so because people in the ancient world perceived a multitude of divine beings as real things to which they related in various forms. One important form of relating to the gods was kinship, this means, imagined divine ancestry which was often used to create social bonds. 

### LANGUAGE

The category **LANGUAGE** includes terms that denote both languages and the dialects of any language.

### GPE and LOC

As **GPE** are annotated the names of any city, nation, empire, city-state, while the label **LOC** is used to annotate mountains, caves, bodies of water, and any location that is not a city, nation, or empire. Note that *ethnonyms*, like *Athenians*, that are sometimes used to denote places are annotated as **NORP** to avoid inconsistencies in the annotation schema. For instance, in a sentence like "The messenger went to the Egyptians",  Egyptians is labeled as **NORP** and not **GPE**, although 'Egyptians' here denotes Egypt.

### PERSON

The label person is applied to proper names or substantivized adjectives that denote individuals. For the latter case see above under **NORP**. 





 



