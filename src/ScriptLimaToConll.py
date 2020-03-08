# !/usr/bin/python
# coding=utf-8
import os
import sys

# On définit les fichiers d'entrée et de sortie
# On récupère le path du fichier auquel il faut extraire des phrases
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# Variable utilisée pour savoir s'il s'agit d'un début de mot/line
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

# On lit le fichier d'entré
with open(inputFile) as fileRead:
    with open(outputFile, 'w') as fileWrite:
        line = fileRead.readline()
        while line:
            # On vérifie si la ligne lue n'est pas un commentaire ou une ligne vide
            if(line[0].isdigit()):
                attributes = line.split('\t')
                word = attributes[1]
                tmpNE = attributes[9].split('|')[0]
                # IF NE IS DETECTED BY LIMA
                if (tmpNE.startswith('NE=')):
                    # WRITE : word - CoNLLTag
                    previousTag = tmpNE.split('=')[1].split('.')[1]
                    # On detecte s'il sagit d'un B (begining) ou I (inside) à l'aide de la variable previousTag
                    if (previousTag != lastLineTag):
                        isBegining = True
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
                # IF NO NE IS DETECTED BY LIMA
                else:
                    # WRITE : word - O
                    #print(word + '\t' + 'O')
                    fileWrite.write(word + '\t' + 'O' + '\n')
                    isBegining = True
            line = fileRead.readline()
