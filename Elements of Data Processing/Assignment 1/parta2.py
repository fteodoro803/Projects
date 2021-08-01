import pandas as pd
import argparse
import matplotlib.pyplot as plt


# FUNCTIONS
# Filtering Dataset File
def datasetFilter(dataset, year=2020):
    filtered_data = dataset.loc[:, ['location', 'date', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]

    filtered_data['date'] = pd.to_datetime(filtered_data['date'], format="%Y-%m-%d")  # converting Object to Datetime

    filtered_data = filtered_data[filtered_data['date'].dt.year == year]  # to include a specific Year

    return filtered_data


# Adjusting Dataset File (To make it per Year, and to aggregate stuff)
def datasetAdjust(dataset):
    dataset['year'] = dataset['date'].dt.year  # adds a corresponding Month column

    # Groups by Location and Month and sums new Cases and Deaths, min_count=1 as to not impute values
    dataset = dataset.groupby(['location', 'year'])[['new_cases', 'new_deaths']].sum(min_count=1)

    # Adds Cumulative Sum columns
    dataset["total_cases"] = dataset.groupby(level=0)["new_cases"].cumsum()
    dataset["total_deaths"] = dataset.groupby(level=0)["new_deaths"].cumsum()

    return dataset


# Case Fatality Rate
def addCaseFatalityRate(dataset):
    dataset['case_fatality_rate'] = dataset['total_deaths'] / dataset['total_cases']
    return dataset


# MAIN
data = pd.read_csv('owid-covid-data.csv', encoding='ISO-8859-1')  # file
data = datasetFilter(data, 2020)  # Filtering through Dataset to get
data = datasetAdjust(data)
data = addCaseFatalityRate(data)
data = data[['case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]  # Rearranging Columns

# Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument(type=str, dest='file1')
parser.add_argument(type=str, dest='file2')
args = parser.parse_args()

# Graphing
caseFatalityRate = data['case_fatality_rate']
confirmedNewCases = data['new_cases']

# Image A
plt.scatter(confirmedNewCases, caseFatalityRate)
plt.xlabel('Confirmed New Cases')
plt.ylabel('Case Fatality Rate')
plt.savefig(args.file1)

# Image B
plt.scatter(confirmedNewCases, caseFatalityRate)
plt.xlabel('Confirmed New Cases')
plt.xscale('log')  # Log Scale
plt.ylabel('Case Fatality Rate')
plt.savefig(args.file2)


"""
External Code References
- Cumulative Sum Code (lines 26 and 27) by Multi-Index Dataframe adapted from
    https://stackoverflow.com/a/23818723, 22 May 2014.
"""
