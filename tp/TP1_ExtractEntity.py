# coding: utf-8
from decimal import *
import sys
getcontext().prec = 3

# On récupère le chemin du fichier d'entré et de sortie
inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

# On initialise un dictionnaire pour compter le nombres d'occurences d'un mots
# Ici key = le mot et value = le nombre d'occurences
wordsDictionnary = dict()
# Cette variable sert à compter le nombre total de mots
nbWords = 0
# On parcourt le fichier d'entrée ligne par ligne
for line in open(inputFilePath, 'r'):
	words = line.split()
	for word in words:
		# Si le mot lu existe déjà dans le dictionnaire on incrémente le compteur du mot
		# Sinon on l'ajoute et on initialise son compteur à 1
		nbWords+=1
  		if word in wordsDictionnary:
			wordsDictionnary[word] += 1
		else:
			wordsDictionnary[word] = 1

print(nbWords)

with open(outputFilePath, 'w') as f:
	# Sert a la mise en forme du fichier de sortie
	f.write('{:>12}  {:>12}  {:>12}  {:>12}\n'.format('Entité nommée','Type','Nombre d’occurrences','Proportion dans le texte (%)'))
	for key, value in wordsDictionnary.iteritems():
		# On parcourt le dictionnaire des occurences
		# On calcul la proportion de présence du mot dans le texte en entier
		tmp = key.split('/')
		WORD = tmp[0]
		TYPE = tmp[1]
		NBOCCURENCES = value
		PROPORTION = (Decimal(value)/Decimal(nbWords))*100
		# On ecrit dans le fichier de sortie
		f.write('{:>12}  {:>12}  {:>12}  {:>12}\n'.format(WORD, TYPE, NBOCCURENCES, PROPORTION))
