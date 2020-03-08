# !/usr/bin/python
# coding=utf-8
import os
import sys

# On stocke ici toutes les ponctuations existantes
ponctuations = '''!()-[]{};:'"\,<>./?@#%^&*_~'''

# On récupère le path du fichier auquel il faut extraire des phrases ainsi que le path du fichier de sortie
inputFile = sys.argv[1]
outputFile = sys.argv[2]

isFirstWordOfSentence = True
# On ouvre le fichier, on le lit ligne par ligne
with open(inputFile) as fp:
    line = fp.readline()
    sentence = ''
    while line:
        if(line != '\n'):
            # Si la ligne récupérée n'est pas vide
            line = line.split('\t')
            if(line[0] != '\n'):
                # Si le mot récupéré n'est pas une ponctuation
                if line[0][0] not in ponctuations:
                    if isFirstWordOfSentence:
                        sentence = sentence + line[0]
                        isFirstWordOfSentence = False
                    else:
                        # On ajout le mot avec un espace s'il ne s'agit pas du premier mot de la ligne
                        sentence = sentence + ' ' + line[0]
                else:
                    # On cole la ponctuation au mot précédent
                    sentence = sentence + line[0]
        else:
            # Si la ligne lue est vide, il s'agit d'une fin de phrase
            # On saute donc une ligne
            sentence = sentence + '\n'
            isFirstWordOfSentence = True
        line = fp.readline()
fp.close
#print(sentence)

with open(outputFile, 'w') as f:
    f.write(sentence)