# !/usr/bin/python
# coding=utf-8
import os
import sys

# On recupere le fichier de resultat lima
limaResultFile = sys.argv[1]
outputFile = sys.argv[2]

lineStartCheck = False

# On lit le fichier d'entré
with open(limaResultFile) as fileRead:
    with open(outputFile, 'w') as fileWrite:
        line = fileRead.readline()
        while line:
            # On vérifie si la ligne lue n'est pas un commentaire ou une ligne vide
            if(line[0].isdigit()):
                word = ''
                posTAG = ''
                lineStartCheck = True
                attributes = line.split('\t')
                # On récupère le mot et le posTAG associé
                word = attributes[1]
                posTAG = attributes[3]
                if (word != '' and posTAG != ''):
                    fileWrite.write(word + '\t' + posTAG + '\n')
            else:
                # Si la ligne lue est vide ou est un commentaire
                # On écrit une ligne vide seulement si on en a pas écrit une précédemment
                if (lineStartCheck):
                    fileWrite.write('\n')
                    lineStartCheck = False
            line = fileRead.readline()
