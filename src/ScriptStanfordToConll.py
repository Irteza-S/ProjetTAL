# !/usr/bin/python
# coding=utf-8
import os
import sys

# On définit les fichiers d'entrée et de sortie
# On récupère le path du fichier auquel il faut extraire des phrases
inputFile = sys.argv[1]
outputFile = sys.argv[2]


# Variable utilisée pour savoir s'il s'agit d'un début de mot
isBegining = True
lastLineTag = ''

# Fonction de convertion Lima -> CoNLL-2003
def tagConverter(i):
    switcher = {
        "PERSON":'-PER',
        "ORGANIZATION":'-ORG',
        "LOCATION":'-LOC',
        "NUMBER":'-MISC',
        "NUMEX":'-MISC',
        "DATE":'-MISC',
    }
    return switcher.get(i,"O")

# On lit le fichier d'entrée ligne par ligne
with open(inputFile) as fileRead:
    with open(outputFile, 'w') as fileWrite:
        line = fileRead.readline()
        while line:
            # On parse le fichier dentree afin de recuperer le mot + tag
            words = line.split(' ')
            for pair in words:
                tmp = pair.split('/')
                # On verifie que la ligne lue est bien compose dun mot + dun tag
                if (len(tmp) == 2):
                    # On recupere le mot et son tag
                    word = pair.split('/')[0]
                    previousTag = pair.split('/')[1]
                    # Avec la variabe previousTag on verifie s'il s'agit ou pas d'un begining/inside
                    if (previousTag != lastLineTag):
                        isBegining = True
                    else:
                        isBegining = False
                    lastLineTag = previousTag
                    # On converti l'ancientag vers le tag CoNLL-2003
                    newTag = tagConverter(previousTag)
                    # On ecrit le mot + le nouveau tag en verifie s'il sagit dun debut B (begining) ou dun I (inside)
                    if (newTag == "O"):
                        isBegining = True
                        fileWrite.write(word + '\t' + newTag + '\n')
                    elif (isBegining == True):
                        newTag = 'B' + newTag
                        isBegining = False
                        fileWrite.write(word + '\t' + newTag + '\n')
                    else:
                        newTag = 'I' + newTag
                        isBegining = False
                        fileWrite.write(word + '\t' + newTag + '\n')
                else:
                    isBegining = True
            line = fileRead.readline()