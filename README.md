# NEReus

#  A Named Entity Corpus of Ancient Greek



NEReus is an annotated corpus of Named Entities in ancient Greek text, developed for the training of neural models. At this point the corpus is an alpha stage and consist only of the annotated version of Herodotus's Histories Book III, which has been revised and has reached the golden standard landmark.  The project aims to to provide NER annotations of the following text in ancient Greek:

* Herodotus' *Histories*, books I, II, III
* Diogenes  Laertius' *Lives of Eminent Philosophers*, books I, III, V, VII
* Selected passages from Pausanias' *Description of Greece*
* Selected passages from Strabo's *Geography*

## Schema

The annotation schema of NEReus consists of the labels **GROUP, GOD, LANGUAGE, PLACE, PERSON** whose description is the following:

### GROUP

The label **GROUP**  refers to adjective which denote:

* Ethnic groups like Greeks, Egyptians, Persians, etc.  **GROUP** contains then *ethnonyms* both in the singular and in the plural.
* *Demonyms*, this is, terms used to denote the natives or inhabitants of a particular city, city-state, or sub-division of a city-state like the *demos* or *tribes* are also labeled as **GROUP**.  
* Other types of social groups, like philosophical schools, religious organizations like *thiasos*, temple personnel, groups of doctors, and similar are also labeled as **GROUP**.
* **<u>Exceptions</u>** are substantivized adjectives in the singular that function as a proper noun like in "the Phoenician". Such cases are labeled as **PERSON** , including the article as in ὁ Φοῖνιξ.

### GOD

In contrast to  modern NER corpora, **NEReus** annotates the names of gods and other supernatural beings. This is so because people in the ancient world perceived a multitude of divine beings as real things to which they related in various forms. One important form of relating to the gods was kinship, this means, imagined divine ancestry which was often used to create social bonds. 

### LANGUAGE

The category **LANGUAGE** includes terms that denote both languages and the dialects of any language.

### PLACE

As **PLACE** are annotated the names of any localities including continents, nations, empires, city-states, mountains, caves, rivers, and so on. However, *ethnonyms* that are used to denote places are annotated as **GROUP** to avoid inconsistencies in the annotation schema. For instance, in a sentence like "The messenger went to the Egyptians",  Egyptians is labeled as **GROUP**.

### PERSON

The label person is applied to proper names or substantivized adjectives that denote individuals. For the latter case see above under **GROUP**. 





 



