# !/usr/bin/python
# coding=utf-8
import nltk
import sys
import os
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import RegexpParser


# On définit les fichiers d'entrée et l'id du pattern souhaité
inputFile = sys.argv[1]
patternId = sys.argv[2]

# Tableau servant a selectionner un pattern
patternSelector = [
"Compound: {<DT>?<JJ>?<NN>}",
"Compound: {<JJ>?<NN>}",
"Compound: {<NN>*<NN>}",
"Compound: {<JJ>?<NN>?<NN>}",
"Compound: {<JJ>?<JJ>?<NN>}",
]


#Lecture du fichier + tokenisation + tags
with open(inputFile, 'r') as myfile:
	data = myfile.read()
	print(data)
	print('\n')
	tokens = word_tokenize(data)
	print(tokens)
	print('\n')
	tokens_tags = pos_tag(tokens)
	print(tokens_tags)
	patterns = patternSelector[int(patternId)]
	chunker = RegexpParser(patterns)
	output = chunker.parse(tokens_tags)
	print('\n')
	print(output)
	output.draw()
myfile.close()
