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
* Apollodorus' Library
  * [ ] Book I
* [ ] Selected passages from Pausanias' *Description of Greece*
* [ ]  Selected passages from Strabo's *Geography*

## Schema

The annotation schema of NEReus consists of the labels **GOD, LANGUAGE, LOC,NORP, PERSON** whose description is the following:

### NORP

The label **NORP**  refers to adjectives that denote:

* Ethnic groups like Greeks, Egyptians, Persians, etc.  **NORP** contains then *ethnonyms* both in the singular and the plural.
* *Demonyms*, this is, terms used to denote the natives or inhabitants of a particular city, city-state, or sub-division of a city-state like the *demos* or *tribes* are also labeled as **NORP**   
* Other social groups, like philosophical schools, religious organizations like *thiasi*, organized temple personnel, groups of doctors, and similar, are also labeled as **NORP**.
* **<u>Exceptions</u>** are substantivized adjectives in the singular that function as a proper noun like in ὁ Φοῖνιξ, "the Phoenician." Such cases are labeled as **PERSON**,  and the label must include the article, as is the case of ὁ Φοῖνιξ.

### GOD

In contrast to  modern NER corpora, **NEReus** annotates the names of gods and other supernatural beings. This is so because people in the ancient world perceived many divine beings as real things to which they related in various forms. A critical form of relating to the gods was kinship: some individuals, for instance, imagined that they had divine ancestry.

### LANGUAGE

The category **LANGUAGE** includes terms denoting both languages and any language's dialects.

### LOC

As **LOC** are annotated the names of cities, nations, empires, and city-states. The label **LOC** is also used to annotate mountains, caves, bodies of water, and any location. Note that *ethnonyms*, like *Athenians*, sometimes used to denote places, are annotated as **NORP** to avoid inconsistencies. For instance, in a sentence like "The messenger went to the Egyptians,"  Egyptians are labeled as **NORP** and not **LOC**, although 'Egyptians' here denotes Egypt. However, in the case of rivers, seas, and territories, more than one token may be annotated as **LOC**. For instance, phrases like the *Nile river* both Nile and river are annotated as one unit. This practice is conveniant in cases like *Assyrian territory* in which both terms need to included in the label **LOC**, otherwise *Assyrian* will be interpreted as a **NORP** entity, which is incorrect. Finally, some names of gods need to be annotated as **LOC** because they denote a place like in the sentence "He went to Hades", where Hades clearly indicates a location and not a god. 

### PERSON

The label person is applied to proper names or substantivized adjectives that denote individuals. For the latter case, see above under **NORP**. 

## Non-Named Entities

For literary studies Named Entitiy Recognition is not enough as researchers may want to explore which animals, smells, and emotions are associated with cerain places and peoples. So, in the feature I plan to add annotation of non-named entities to the dataset. 





 
