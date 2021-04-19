# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:13:49 2021

@author: gianm
"""

#Class untuk membuat dictionary yang berisi POS dan jumlah kemunculannya

from nltk import sent_tokenize, word_tokenize, pos_tag
import re
import pickle

textFile = ''
sentence_list = list()
taggedSentences = list()

#%% import file
def openFile(fileName):
    global textFile
    textFile = open('{}.txt'.format(fileName), 'r').read()

#%% tokenize
def tokenize_sentence():
    global sentence_list
    #Tokenize text berdasarkan kalimat
    sentences = sent_tokenize(textFile)
    #Bersihkan kalimat, buang semua tanda baca
    sent_list = list()
    for i in sentences:
        sent_list.append(re.sub('[^A-Za-z0-9\-\. ]', '', i).lower())
    sentence_list = sent_list

#%% tokenize (2)
def tag_sentences():
    global taggedSentences
    #list berisi list kata-kata yang telah di tokenisasi
    tokenizedSentences = [word_tokenize(sent) for sent in sentence_list]
    #berikan label POS untuk setiap kata
    taggedSentences = [pos_tag(stc, tagset='universal') for stc in tokenizedSentences]

if __name__ == '__main__':
    fileName = input('file name:')
    openFile(fileName)
    tokenize_sentence()
    tag_sentences()
    
    #simpan file yang telah dibuat dengan pickle dengan pickle
    pickle.dump(fileName, open('file_name.pickle', 'wb'))
    pickle.dump(taggedSentences, open('tagged_sentence.pickle', 'wb'))
    




        
    
        
    

