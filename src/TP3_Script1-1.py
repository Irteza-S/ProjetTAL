import nltk
import sys
import os
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk import pos_tag

inputFile = sys.argv[1]
outputFile = sys.argv[2]

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


print('\n')

with open(outputFile, 'w') as fp:
	for pair in tokens_tags:
		fp.write(pair[0] + '\t' + pair[1] + '\n')

