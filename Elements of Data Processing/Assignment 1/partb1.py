# Part B Task 1

import re
import pandas as pd
import os
import argparse

# Constants
fileExtensionPattern = r'.txt$'  # checks if file ends with .txt
idPattern = r'[a-zA-Z]{4}-\d{3}[a-zA-Z]?'
ID_MAX_LENGTH_OPTION = 9  # 4 Letters + 1 Hyphen + 3 Numbers + 1 Optional Letter, according to Spec
ID_MAX_LENGTH_NO_OPTION = 8  # 4 Letters + 1 Hyphen + 3 Numbers, according to Spec

# Initialising DataFrame
data = {}
idDataFrame = pd.DataFrame(data, columns=['filename', 'documentID'])

# Going through Files in Cricket Directory
for fileName in os.listdir('cricket'):
    f = open(os.path.join('cricket', fileName), 'r')
    file = f.read()

    if re.search(idPattern, file):  # Checks if Pattern is in File
        patternSearch = re.search(idPattern, file)  # to get Span
        rawID = file[patternSearch.start():patternSearch.end() + 5]  # arbitrary +5 to see how long string continues
        idList = re.split(r'[\s]', rawID)  # Tokenises String on possible Spacing

        # Assumption: unique presence of id-esque-string, so it's first on the list, hence idList[0]
        currentID = idList[0]
        idLength = len(idList[0])

        # Identifying the Article ID
        if idLength > ID_MAX_LENGTH_OPTION:
            # Assumption: If there are two CAPS letters, the second letter indicates start of Sentence; first stays
            if currentID[ID_MAX_LENGTH_OPTION-1].isupper() and currentID[ID_MAX_LENGTH_OPTION].isupper():
                finalID = currentID[0:ID_MAX_LENGTH_OPTION]
            else:
                finalID = currentID[0:ID_MAX_LENGTH_NO_OPTION]
        elif idLength == 9:
            finalID = currentID[0:ID_MAX_LENGTH_OPTION]
        elif idLength == ID_MAX_LENGTH_NO_OPTION:
            finalID = currentID[0:ID_MAX_LENGTH_NO_OPTION]

        # Appending the Data into Dataframe
        newRow = {'filename': fileName, 'documentID': finalID}
        idDataFrame = idDataFrame.append(newRow, ignore_index=True)

    f.close()

# Command Line Arguments and saving as CSV
parser = argparse.ArgumentParser()
parser.add_argument('fileName', type=str)
args = parser.parse_args()
outputFile = args.fileName
idDataFrame.to_csv(outputFile, index=False)  # Saving Database
