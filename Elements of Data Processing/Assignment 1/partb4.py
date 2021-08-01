# Part B Task 4
import re
import pandas as pd
import os
import sys
import nltk


# FUNCTIONS
# Stores Keywords from Arguments
def getKeyWords():
    key_words = []
    for i in range(len(sys.argv)-1):  # -1 to ignore the 'partb3.py' from command line
        key_words.append(sys.argv[i+1].lower())  # +1 to ignore the 'partv3.py' from command line

    return key_words


# Preprocesses Files according to Spec (from partb2.py)
def filePreprocessing(file):
    new_file = re.sub(r'[^\sA-Za-z]', ' ', file)  # removes non-Alphabetic Characters and non-Whitespace Characters
    new_file = re.sub(r'\s', ' ', new_file)  # makes every Whitespace Character a singular Whitespace
    new_file = re.sub(' +', ' ', new_file)  # changes remaining consecutive Whitespaces into a single Whitespace
    new_file = new_file.lower()  # removes Lowercase Characters

    return new_file


# Converts the Words in the File into Stemmed-equivalents
def fileStem(file):
    porter_stemmer = nltk.PorterStemmer()
    split_words = file.split()
    stem_words = []

    # Getting the Stem of each Word
    for word in split_words:
        stem_words.append(porter_stemmer.stem(word))

    return ' '.join(stem_words)


# MAIN
porterStemmer = nltk.PorterStemmer()
keyWords = getKeyWords()

documentIDs = pd.read_csv('partb1.csv')
documentIDs = documentIDs.set_index(documentIDs['filename'])

directory = os.listdir('cricket')

for fileName in directory:
    f = open(os.path.join('cricket', fileName), 'r')
    file = filePreprocessing(f.read())

    matchCounter = 0  # for checking the Number of Matches to the Number of Queries

    # Finds Matches from a File to the Pattern
    for key in keyWords:
        pattern = rf'\b{key}\b'  # to ensure there is a space on both Sides, meaning it's a Word
        patternStem = rf'\b{porterStemmer.stem(key)}\b'

        if re.search(pattern, file) or re.search(patternStem, file):
            matchCounter += 1
        else:  # on the Chance that Stemming didn't work Perfectly on either the Keywords or the Document
            fileStemmed = fileStem(file)
            if re.search(pattern, fileStemmed) or re.search(patternStem, fileStemmed):
                matchCounter += 1
            else:
                break  # if missing a match, skips current File

        if matchCounter == len(keyWords):  # number of Queries in File
            print(documentIDs.loc[fileName, 'documentID'])

    f.close()
