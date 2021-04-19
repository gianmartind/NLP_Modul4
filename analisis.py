# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:36:45 2021

@author: gianm
"""

#%% analisis 
import pickle

#import file pickle
taggedSentences = pickle.load(open('tagged_sentence.pickle', 'rb'))

#Hitung jumlah kemunculan setiap tag POS di dokumen
pos_dict_2 = dict()
for sent in taggedSentences:
    for a, b in sent:
        if b != '.':
            if b in pos_dict_2:
                pos_dict_2[b] = pos_dict_2[b] + 1
            else:
                pos_dict_2[b] = 1
    
#%% Visualisasi 
import matplotlib.pyplot as plt

keys = list(pos_dict_2.keys())
values = list(pos_dict_2.values())

fileName = pickle.load(open('file_name.pickle', 'rb'))

plt.pie(values, labels=keys)
plt.title(fileName)
plt.show()
