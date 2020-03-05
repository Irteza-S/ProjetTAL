# Projet TAL

2019 - 2020 ET5 Polytech Paris Sud

Enseignant : 

Groupe :


## Pré-requis

Ubuntu 16.04 LTS et Python2.7

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.


## Projet
1 - Evaluation de l’analyse morpho-syntaxique

1)  Convertir les tags du corpus "pos_reference.txt.lima" en tags universels

    Pour convertir les tags du corpus LIMA en tags universels, il faut d'abords convertir les tags du corpus LIMA en tags PTB. Puis il faut convertir les tags PTB obtenus en tags universels.
    Pour réaliser ces conversions, il faut utiliser le script ScriptLimaToUniversal.py. Ce script prend 4 paramètres : le premier est le fichier Lima à convertir, le deuxième est le dictionnaire de conversion LIMA vers PTB (POSTAG...), le troisième est le dictionnaire de conversion PTB vers universel (POSTAg....) et le dernier paramètre est le nom du fichier de sortie dans lequel on retrouvera les résultats de la conversion LIMA vers Universel.

    Exemple d'utilisation :

```bash
-> python2.7 ScriptLimaToUniversal.py pos_reference.txt.lima POSTags_LIMA_PTB_Linux.txt POSTags_PTB_Universal_Linux.txt pos_reference.txt.univ
```

2)  Extraire les phrases du corpus "pos_reference.txt.univ"

    Pour extaire les phrases du corpus "pos_reference.txt.univ", il faut lire ligne par ligne ce fichier. Lorsque la ligne lue est vide, on considère qu'il s'agit d'une fin de phrase, lorsque la ligne lue n'est pas vide on ajout le mot à la ligne courante lue. Pour réaliser cette extraction, on utilise le script "ScriptExtractor.py". Ce script prend 2 paramètres : le premier est le fichier duquel il faut extraire les phrases et le deuxième est le fichier dans lequel va se trouver le résultat de cette extraction.

    Exemple d'utilisation :

```bash
-> python2.7 ScriptExtractor.py pos_reference.txt.lima post_test.txt
```


