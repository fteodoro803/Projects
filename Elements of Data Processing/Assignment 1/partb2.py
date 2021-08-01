# Part B Task 2
import re
import os
import sys


# FUNCTIONS
# Preprocesses Files according to Spec
def filePreprocessing(file):
    new_file = re.sub(r'[^\sA-Za-z]', ' ', file)  # removes non-Alphabetic Characters and non-Whitespace Characters
    new_file = re.sub(r'\s', ' ', new_file)  # makes every Whitespace Character a singular Whitespace
    new_file = re.sub(r' +', ' ', new_file)  # changes remaining consecutive Whitespaces into a single Whitespace
    new_file = new_file.lower()  # removes Lowercase Characters

    return new_file


# MAIN
directory = os.listdir('cricket')  # Directory where File is located, according to Spec
fileName = sys.argv[1]  # the File to be Processed

# Opening and Processing File
f = open(os.path.join('cricket', fileName), 'r')
sourceFile = f.read()
adjustedFile = filePreprocessing(sourceFile)
print(adjustedFile)
f.close()
