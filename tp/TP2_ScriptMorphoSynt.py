# !/usr/bin/python
# coding=utf-8
import os
import sys

# On définit les fichiers d'entrés et de sortie
# On récupère le path du fichier auquel il faut extraire des phrases
inputFile = sys.argv[1] # './wsj_0010_sample.txt.conllu'
outputFile = sys.argv[2] # './wsj_0010_sample.txt.pos.lima'

# On ouvre le fichier de sortie
outputFile = open(outputFile, 'w')

# On parcourt le fichier d'entree
with open(inputFile, 'r') as inFile:
    lines = inFile.readlines()
    for line in lines:
        # On parse la ligne
        words = line.split()
        # On verifie que la ligne nest pas vide
        if words:
            # On nextrait la ligne que si il ne sagit pas dun nombre, dun commentaire ou autre chose
            if(words[0].isdigit()):
                mot = words[1]
                etiquette = words[3]
                outputFile.write(mot + '\t' + etiquette + '\n')
outputFile.close()
