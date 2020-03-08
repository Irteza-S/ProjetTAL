# !/usr/bin/python
# coding=utf-8
import os
import sys

# On définit le fichier a convertir ainsi que celui de sortie et de reference
fileToConvert = sys.argv[1]
refFile = sys.argv[2]
newFile = sys.argv[3]


universalDictionnary = {}

# On stocke dans le dictionnaire universel les mots et les tags du fichier de reference
with open(refFile, 'r') as refFileRead:
	# On lit le fichier de reference et on stocke le mot + tag
	line = refFileRead.readline()
	while (line):
		words = line.split()
		word = words[0]
		tag = words[1]
		universalDictionnary[word] = tag
		line = refFileRead.readline()

print(universalDictionnary)
print('\n')

# On ouvre le fichier a convertir
with open(fileToConvert, 'r') as convertFileRead:
	with open(newFile, 'w') as newFileWrite:
		# On parcourt le fichier a convertir
		line = convertFileRead.readline()
		while (line):
			# Pour chaque tag lu, on le convertit
			words = line.split()
			word = words[0]
			tag = words[1]
			newTag = universalDictionnary.get(tag)
			# Si la convertion fonctionne on ecrit dans le nouveau fichier
			if newTag is not None:
				newFileWrite.write(word + '\t' + newTag + '\n')
			line = convertFileRead.readline()


