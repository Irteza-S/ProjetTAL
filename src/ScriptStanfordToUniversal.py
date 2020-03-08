# !/usr/bin/python
# coding=utf-8
import os
import sys

stanfordFile = sys.argv[1]
universalFile = sys.argv[2]
outputFile = sys.argv[3]

# On stocke les tags Universel dans un dictionnaire
universalDictionnary = {}
with open(universalFile, 'r') as refFile:
	line = refFile.readline()
	while (line):
		words = line.split()
		word = words[0]
		tag = words[1]
		universalDictionnary[word] = tag
		line = refFile.readline()
refFile.close
print(universalDictionnary)
print('\n')

# On lit le fichier stanford
# On récupère l'ancien tag
# à l'aide du dictionnaire des tags universels, on obtiens le nouveau tag
with open(stanfordFile, 'r') as oldFile:
    with open(outputFile, 'w') as newFile:
        line = oldFile.readline()
        while (line):
            # On récupère le block de résultat
            # 1 block = 1 phrase
            block = line.split()
            i = 0
            # On parcourt le block pour y extraire les mots et leur tag
            while (i < len(block)):
                pair = block[i]
                word = pair.split('_')[0]
                tag = pair.split('_')[1]
                # On convertit l'ancien tag vers un tag universel
                universalTag = universalDictionnary.get(tag)
                # Si un tag à été trouvé
                if universalTag is not None:
                    newFile.write(word + '\t' +universalTag + '\n')
                i += 1
                # Lorsque l'on a atteint la fin d'un block
                # on saute une ligne (fin de phrase)
                if(i == len(block)):
                    newFile.write('\n')
            line = oldFile.readline()
oldFile.close
newFile.close