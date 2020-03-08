#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:35:23 2020

@author: mkhamis
"""
# !/usr/bin/python
# coding=utf-8
import os
import sys
from xml.dom import minidom
import xml.etree.ElementTree as ET

# On définit les fichiers d'entrés et de sortie
# On récupère le path du fichier auquel il faut extraire des phrases
inputFile = sys.argv[1] # " wsj_0010_sample.txt.se.xml"
outputFilePath = sys.argv[2] # "extracted-data.txt"


tree = ET.parse(inputFile)
root = tree.getroot()

# Dict of dict to be able to store data
data = {'Organization.ORGANIZATION' : {},
'Person.PERSON' : {},
'Location.LOCATION' : {}}

nbValues = 0;
# Iterate through every entity
for specific_entity in root.iter('specific_entity'):
    nbValues = nbValues + 1;
    type = specific_entity.find('type').text;
    # Checking if named entity
    if type=="Organization.ORGANIZATION" or   type=="Person.PERSON" or type=="Location.LOCATION":
        name = specific_entity.find('string').text
        # Does it exist
        if name in data[type]:
            data[type][name] = data[type][name] + 1;
        else:
            data[name] = 1;
            data[type][name] = 1;

nbValues = nbValues - 2;
# Ecrire la sortie     
with open(outputFilePath, 'w') as f:
	f.write('{:>25}  {:>25}  {:>25}  {:>25}\n'.format('Entité nommée','Type','Nombre d’occurrences','Proportion (%)'))
	for type in ["Organization.ORGANIZATION", "Person.PERSON", "Location.LOCATION"]:
            for name in data[type] :
                f.write('{:>25}  {:>25}  {:>25}  {:>10}/{:>1}={:>3}%\n'.format(name, type, str(data[type][name]),str(data[type][name]),nbValues,str((int(data[type][name])*100)/nbValues)))
               
                
#, str((int(data[type][name])*100)/nbValues)))
