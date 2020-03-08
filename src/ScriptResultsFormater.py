# !/usr/bin/python
# coding=utf-8
import os
import sys

# Récupération de l'ancien fichier ainsi que du fichier de référence
oldFileToConvert = sys.argv[1]
refFile = sys.argv[2]
newConvertedFile = sys.argv[3]
newRefFile = sys.argv[4]

# On definit deux dictionnaires
refFileDictionnary = []
oldFileDictionnary = []

# On stocke tout les mots de Ref
with open(refFile, 'r') as refFileRead:
    line = refFileRead.readline()
    # On parcourt tout le fichier de référence et on stocke tout les mots et leur tag
    while (line):
        words = line.split('\t')
        if (len(words) != 1):
            word = words[0]
            tag = words[1].split('\n')[0]
            refFileDictionnary.append((word, tag))
           #print(word + ' ' + tag)
        line = refFileRead.readline()
refFileRead.close()
#print(refFileDictionnary)

# On stocke tout les mots de lima/stanford/nltk
with open(oldFileToConvert, 'r') as oldFileRead:
    line = oldFileRead.readline()
    # On parcourt tout le fichier lima/stanford/nltk et on stocke tout les mots et leur tag
    while (line):
        words = line.split('\t')
        if (len(words) != 1):
            word = words[0]
            tag = words[1].split('\n')[0]
            oldFileDictionnary.append((word, tag))
           #print(word + ' ' + tag)
        line = oldFileRead.readline()
oldFileRead.close()
#print(oldFileDictionnary)


# On vérifie que les mots de ref sont présents chez lima/stanford auquel cas on écrit dans les nouveaux fichiers
with open(newRefFile, 'w') as refFileWrite:
    with open(newConvertedFile, 'w') as newFileWrite:
        # On se base sur le fichier de reference
        for refPair in refFileDictionnary:
            word = refPair[0]
            # Si le mot lu depuis le fichier de référence est contenu dans le fichier lima/stanford/nltk alors on l'écrit
            # On s'assure ainsi d'avoir les mêmes mots sur les deux fichiers
            result = [x for x in oldFileDictionnary if x[0] == word]
            if (len(result) != 0):
                refFileWrite.write(refPair[0] + '\t' + refPair[1] + '\n')
                newFileWrite.write(result[0][0] + '\t' + result[0][1] + '\n')