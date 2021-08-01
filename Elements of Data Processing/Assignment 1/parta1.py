import pandas as pd
import argparse


# FUNCTIONS
# A1.1 Filtering Dataset File
def datasetFilter(dataset, year=2020):
    filtered_data = dataset.loc[:, ['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

    filtered_data['date'] = pd.to_datetime(filtered_data['date'], format="%Y-%m-%d")  # converting Object to Datetime

    filtered_data = filtered_data[filtered_data['date'].dt.year == year]  # to include a specific Year

    return filtered_data


# A1.2 Adjusting Dataset File (To make it per Month, and to aggregate stuff)
def datasetAdjust(dataset):
    dataset['month'] = dataset['date'].dt.month  # adds a corresponding Month column

    # Groups by Location and Month and sums new Cases and Deaths, min_count=1 as to not impute values
    dataset = dataset.groupby(['location', 'month'])[['new_cases', 'new_deaths']].sum(min_count=1)

    # Adds Cumulative Sum columns
    dataset["total_cases"] = dataset.groupby(level=0)["new_cases"].cumsum()
    dataset["total_deaths"] = dataset.groupby(level=0)["new_deaths"].cumsum()

    return dataset


# A2 Case Fatality Rate
def addCaseFatalityRate(dataset):
    dataset['case_fatality_rate'] = dataset['total_deaths'] / dataset['total_cases']
    return dataset


# MAIN
data = pd.read_csv('owid-covid-data.csv', encoding='ISO-8859-1')  # file
data = datasetFilter(data, 2020)  # Filtering through Dataset to get
data = datasetAdjust(data)
data = addCaseFatalityRate(data)
data = data[['case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]  # Rearranging Columns

print(data.head(5))  # Printing the first 5 Rows

# Command Line Arguments and saving as CSV
parser = argparse.ArgumentParser()
parser.add_argument('fileName', type=str)
args = parser.parse_args()
outputFile = args.fileName
data.to_csv(outputFile)  # Saving Database

"""
External Code References
- Cumulative Sum Code (lines 25 and 26) by Multi-Index Dataframe adapted from
    https://stackoverflow.com/a/23818723, 22 May 2014.
"""
