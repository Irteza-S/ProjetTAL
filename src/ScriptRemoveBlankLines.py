# !/usr/bin/python
# coding=utf-8
import os
import sys

# On recupere le fichier d'entré et l'emplacement du fichier de sortie
inputFile = sys.argv[1]
outputFile = sys.argv[2]


# On lit le fichier d'entré
with open(inputFile, 'r') as fileRead:
    with open(outputFile, 'w') as fileWrite:
        line = fileRead.readline()
        while line:
            if(line != '\n'):
                fileWrite.write(line)
            line = fileRead.readline()
fileRead.close
fileWrite.close