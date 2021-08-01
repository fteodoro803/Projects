# Part B Task 5
import re
import os
import sys
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
import math
from numpy import dot
from numpy.linalg import norm


# FUNCTIONS
# Stores Keywords from Arguments
def getKeyWords():
    key_words = []
    for i in range(len(sys.argv) - 1):  # -1 to ignore the 'partb3.py' from command line
        key_words.append(sys.argv[i + 1].lower())  # +1 to ignore the 'partv3.py' from command line

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


# Compiles Key Words in each Document
def getMeaningfulWords(file_dictionary):
    # nltk.download('stopwords')  #if downloading for first time
    # nltk.download('punkt')
    porter_stemmer = nltk.PorterStemmer()
    stop_words = set(stopwords.words('english'))

    filtered_list = []  # Words that aren't Stopwords
    for file in file_dictionary:  # files will become matchedFiles
        for word in nltk.word_tokenize(file_dictionary[file]):
            if word not in stop_words:
                filtered_list.append(word)

    key_word_list = []  # Important Words in Document
    for word in filtered_list:
        stem_word = porter_stemmer.stem(word)
        if stem_word not in key_word_list:
            key_word_list.append(stem_word)

    return key_word_list


# Compiles Word Counts from each Document
def getWordCounts(file_dictionary, word_list):
    file_word_counts = {}

    for file in file_dictionary:
        file_word_counts[file] = dict.fromkeys(word_list, 0)  # initialises count to 0

        # Gets the Counts
        for word in nltk.word_tokenize(file_dictionary[file]):
            if word in word_list:
                file_word_counts[file][word] += 1

    return file_word_counts


# Generates TF-IDF
def getTFIDF(word_count_dictionary):
    term_counts = []  # List of Matches of each Word in Documents according to Query
    for file in word_count_dictionary:
        term_counts.append(list(word_count_dictionary[file].values()))  # converts Dictionary of Values into List

    transformer = TfidfTransformer()
    tfidf_transformation = transformer.fit_transform(term_counts)

    return tfidf_transformation


# Derives Query Vector
def getQueryVector(query_list, word_list_dictionary):
    query_vector = dict.fromkeys(word_list_dictionary, 0)  # initialising Query Vector to 0
    for word in query_list:
        if word in query_vector:
            query_vector[word] = 1
    query_vector = list(query_vector.values())  # converting Dictionary to Array

    # Query Unit Vector
    length_query_vector = 0
    for num in query_vector:
        length_query_vector += num

    if length_query_vector == 0:  # in the Case of no Matches
        print(f"No Match for {query_list}")
        quit()

    query_unit_vector = [x / (math.sqrt(length_query_vector)) for x in query_vector]
    return query_unit_vector


# Calculates Cosine Similarity
def cosineSimilarity(vector1, vector2):
    return dot(vector1, vector2) / (norm(vector1) * norm(vector2))


# Gets Cosine Similarity Scores for each Document according to Query
def getSimilarityScores(matched_files_dictionary, tf_idf, query_unit_vector):
    similarityScoresDictionary = {}

    for document in range(tf_idf.toarray().shape[0]):
        document_id_list = list(matched_files_dictionary.keys())[document]
        similarityScoresDictionary[document_id_list] = round(cosineSimilarity(query_unit_vector,
                                                                              tf_idf.toarray()[document]), 4)
                                                                            # make to dictionary then convert to series

    # Turns it into a Pandas DataFrame
    similarity_scores_pandas = pd.DataFrame(list(similarityScoresDictionary.items()),
                                            columns=['documentID', 'score'])
    similarity_scores_pandas = \
        similarity_scores_pandas.sort_values('score', ascending=False)  # sort by Score in Descending Order

    return similarity_scores_pandas


# MAIN
porterStemmer = nltk.PorterStemmer()
keyWords = getKeyWords()  # Query Words for Search

documentIDs = pd.read_csv('partb1.csv')
documentIDs = documentIDs.set_index(documentIDs['filename'])
directory = os.listdir('cricket')

matchedFiles = {}  # for Files matching Keywords, for Scoring

# Searching for Matches
for fileName in directory:
    f = open(os.path.join('cricket', fileName), 'r')
    file = filePreprocessing(f.read())

    matchCounter = 0  # for checking the Number of Matches to the Number of Queries

    # Finds Matches from a File to the Pattern
    for key in keyWords:
        pattern = rf'\b{key}\b'  # to ensure there is a space on both Sides, meaning it's a Word
        patternStem = rf'\b{porterStemmer.stem(key)}\b'
        fileStemmed = fileStem(file)

        if re.search(patternStem, fileStemmed):
            matchCounter += 1
        else:
            break  # if missing a match, skips current File

        if matchCounter == len(keyWords):  # number of Queries in File
            matchedFiles[documentIDs.loc[fileName, 'documentID']] = fileStemmed

    f.close()

query = []
for word in keyWords:  # makes Keywords into Stemmed Versions for Scoring Purposes
    query.append(porterStemmer.stem(word))

# Scoring Matches
wordList = getMeaningfulWords(matchedFiles)
wordCounts = getWordCounts(matchedFiles, wordList)
tfidf = getTFIDF(wordCounts)
queryUnitVector = getQueryVector(query, wordList)
similarityScores = getSimilarityScores(matchedFiles, tfidf, queryUnitVector)

print(similarityScores.to_string(index=False))

"""
External Code References.
- getMeaningfulWords() by the University of Melbourne adapted from 2021s1_workshop4_solutions.ipynb, 30 March 2021
- getTFIDF by the University of Melbourne adapted from Lecture 4, Part 7: Unstructured Data - Text Representations, 2021
- getQueryVector() by the University of Melbourne adapted from 
    Lecture 4, Part 7: Unstructured Data - Text Representations, 2021
- cosineSimilarity() by the University of Melbourne adapted from 
    Lecture 4, Part 7: Unstructured Data - Text Representations, 2021
- getSimilarityScores() by the University of Melbourne adapted from 
    Lecture 4, Part 7: Unstructured Data - Text Representations, 2021
"""
