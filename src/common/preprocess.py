"""
preprocess.py

This script must be run before anything else.
Functions:
    - loads data file into a matrix
    - splits the matrix into 90% training data, 10% test data (rows selected randomly)
    - create dictionary of feature labels and associated variable names
"""
import pandas
import numpy
from sklearn.model_selection import train_test_split

"""
Imports CSV file with specified @param filename,
stores it as a Pandas dataframe called data
and then cleans the data to remove rows with missing test scores
"""
def load_data_file(filename):
    data = pandas.read_csv(filename)
    initial_size = data.shape[0]
    # drop the rows of the dataframe that are missing the average test scores since this is vital info
    data = data.dropna(subset=['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE'])
    cleaned_size = data.shape[0]
    print(str(initial_size - cleaned_size) + " rows removed because of missing data.")
    print(str(cleaned_size) + " rows remaining.")
    return data

"""
Splits the given Pandas dataframe @param data into 2 sets -
90% training data, 10% test data (with rows selected randomly)
"""
def split_into_training_and_test(data):
    training_data, test_data = train_test_split(data, test_size=0.1)
    # print statements are mostly just for sanity check
    print(str(training_data.shape[0]) + " rows in training data.")
    print(str(test_data.shape[0]) + " rows in test data.")
    return training_data, test_data