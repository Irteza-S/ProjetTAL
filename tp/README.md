# ProjetTAL/tp

Ce dossier contient les codes sources des script Python des trois TP

## Pré-requis

Ubuntu 16.04 LTS et Python2.7

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.


## TP1
1 - Installation et évaluation de l’outil de désambiguïsation morpho- syntaxique de l’université de Stanford

2)  Evaluation sans étiquettes universelles

    Pour comparer les fichiers wsj_0010_sample.txt.pos.stanford et wsj_0010_sentence.pos.ref, il faut que les deux fichiers soient aux même format. Pour cela on utilise le script nommé TP1_1.py en rensaignant 2 paramètres : le premier est le path vers le fichier wsj_0010_sample.txt.pos.stanford et le deuxième est le fichier de sorti converti au bon format.
    
    Exemple :

```bash
-> python2.7 script1.py wsj_0010_sample.txt.pos.stanford wsj_0010_sample_converted.txt.pos.stanford
```

2)  Evaluation avec étiquettes universelles wsj_0010_sample.txt.pos.stanford et wsj_0010_sentence.pos.ref (s'assurer au préalable qu'ils sont tout les deux au bon format), on utilise le script nommé UniversalConverter.py qui prend 3 paramètres : le premier est le path vers le fichier à convertir, le deuxième est le fichier de référence et le troisième est le fichier de sorti

    Exemple :

```bash
-> python2.7 UniversalConverter.py wsj_0010_sample_edited.txt.pos.stanford POSTags_PTB_Universal_Linux.txt tmp.txt
-> python2.7 UniversalConverter.py wsj_0010_sample.pos.ref POSTags_PTB_Universal_Linux.txt tmp1.txt
```


2 - Extraction d’entités nommées

Il faut lancer le script TP1_ExtractEntity.py avec 2 arguments... :

```bash
-> python2.7 script.py wsj_0010_sample.txt.ner.output k.txt
```


## TP2
2 - Extraction d’entités nommées

Il faut lancer le script TP2_ExtractEntiteNommees.py avec 2 arguments... :

```bash
-> python2.7 TP2_ExtractEntiteNommees.py
```
On obtiens : 


3 - Analyse morpho-syntaxique

Il faut lancer le script TP2_ScriptMorphoSynt.py avec 2 arguments... :

```bash
-> python2.7 TP2_ScriptMorphoSynt.py
```
On obtiens le fichier wsj_0010_sample.txt.pos.lima suivant : 













```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)