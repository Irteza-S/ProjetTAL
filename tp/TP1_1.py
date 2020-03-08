# !/usr/bin/python
# coding=utf-8
import os
import sys

# Récupération de l'ancien fichier ainsi que du fichier de référence
filePath = sys.argv[1] #'./wsj_0010_sample.txt.pos.stanford'
text_file = sys.argv[2] #"./wsj_0010_sample_edited.txt.pos.stanford"

# On parcourt tout le fichier d'entrée
with open(filePath, 'r') as inFile:
    data = inFile.readlines()
    # On parle les lignes du fichiers d'entrée pour récupérer les mots et leur tag
    for i in data:
        pairs = i.split()
        for pair in pairs:
            word = pair.split('_')[0]
            tag = pair.split('_')[1]
            # On écrit sur le fichier de sortie le mot + le tag
            text_file.write(word + '\t' + tag + '\n')
text_file.close()
