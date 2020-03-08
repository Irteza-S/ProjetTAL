# !/usr/bin/python
# coding=utf-8
import os
import sys

# Récupération du fichier résultats brut lima + table de conversion lima vers ptb et ptb vers universel
limaFile = sys.argv[1]
ptbFile = sys.argv[2]
universalFile = sys.argv[3]
outputFile = sys.argv[4]


# On stocke les tags PTB dans un dictionnaire
ptbDictionnary = {}
with open(ptbFile, 'r') as refFile:
	line = refFile.readline()
	while (line):
		words = line.split()
		word = words[0]
		tag = words[1]
		ptbDictionnary[word] = tag
		line = refFile.readline()
refFile.close()
#print(ptbDictionnary)
#print('\n')

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
#rint(universalDictionnary)
#print('\n')

# On lit le fichier lima
# On récupère l'ancien tag
# à l'aide du dictionnaire LIMA vers PTB on obtiens le tag PTB
# à l'aide du dictionnaire PTB vers Unniversal on obtiens le tab universel
with open(limaFile, 'r') as oldFile:
	with open(outputFile, 'w') as newFile:
		line = oldFile.readline()
		while (line):
			words = line.split()
			# On vérifie qu'on a pas lu un saut de ligne
			if(len(words) > 1):
				#print(words)
				word = ''
				limaTag = ''
				# S'il y a plus d'un mot analysé sur la ligne
				if(len(words) > 2):
					size = len(words)
					limaTag = words[size - 1]
					i = 0
					while (i < size - 1):
						if i == 0:
							word = words[i]
						else:
							word = word + ' ' + words[i]
						i += 1
				# Sinon on récupère le mot et le tag
				else:
					word = words[0]
					limaTag = words[1]
				# On convertit le tag lima en PTB
				ptbTag = ptbDictionnary.get(limaTag)
				# On vérifie qu'un tag PTB correspond au tag Lima
				if ptbTag is not None:
					# On convertit le tag PTB en Unniversel
					universalTag = universalDictionnary.get(ptbTag)
					if universalTag is not None:
						# On écrit le tag universel dans le nouveau fichier
						newFile.write(word + '\t' + universalTag + '\n')
					else:
						# On écrit 'None' 
						newFile.write(word + '\t' + 'None' + '\n')
				else:
					# On écrit 'None' 
					newFile.write(word + '\t' + 'None' + '\n')
			else:
				# S'il s'agit d'un saut de ligne on saute une ligne
				newFile.write('\n')
			line = oldFile.readline()
oldFile.close
newFile.close