"""
preprocess.py

This script must be run before anything else.
Functions:
    - loads data file into a matrix
    - splits the matrix into 90% training data, 10% test data (rows selected randomly)
    - create dictionary of feature labels and associated variable names
"""
from sklearn.model_selection import train_test_split
import pandas as pd
import config

"""
Imports CSV file with specified @param filename,
stores it as a Pandas dataframe called data
and then cleans the data to remove rows with missing test scores
"""
def load_data_file(filename):
    data = pd.read_csv(filename)
    initial_size = data.shape[0]
    # drop the rows of the dataframe that are missing the average test scores since this is vital info
    data = data.dropna(subset=['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE'])
    # drop the rows of the dataframe whether other important information is missing (some blank cells are tolerated per row)
    data = data.dropna(subset=['TOTAL_EXPENDITURE', 'FEDERAL_REVENUE', 'STATE_REVENUE'])
    cleaned_size = data.shape[0]
    print(str(initial_size - cleaned_size) + " rows removed because of missing data.")
    print(str(cleaned_size) + " rows remaining.")
    return data

"""
Splits the given Pandas dataframe @param data into 2 sets -
90% training data, 10% test data (with rows selected randomly)
"""
def split_into_training_and_test(data):
    config.TRAINING_DATA, config.TEST_DATA = train_test_split(data, test_size=0.1)
    config.TRAINING_DATA = pd.DataFrame(config.TRAINING_DATA)
    config.TEST_DATA = pd.DataFrame(config.TEST_DATA)
    # replace NaN in dataframes with 0 (for dot product purposes)
    config.TRAINING_DATA.fillna(0)
    config.TEST_DATA.fillna(0)
    # set index of dataframes to be 'PRIMARY_KEY' column
    config.TRAINING_DATA.set_index('PRIMARY_KEY', inplace=True)
    config.TEST_DATA.set_index('PRIMARY_KEY', inplace=True)

    """
    # add Primary Key to dataframes, where primary key is combination
    # of state and year
    pk_training = pd.Series([])
    for i in range(len(config.TRAINING_DATA)):
        pk_training[i] = str(config.TRAINING_DATA['YEAR']) + "_" + str(config.TRAINING_DATA['STATE'])
    config.TRAINING_DATA.insert(0, 'PRIMARY_KEY', pk_training)
    pk_test = pd.Series([])
    for i in range(len(config.TEST_DATA)):
        pk_test[i] = str(config.TEST_DATA['YEAR']) + "_" + str(config.TEST_DATA['STATE'])
    config.TEST_DATA.insert(0, 'PRIMARY_KEY', pk_test)
    """

    # TODO delete later
    with open('training_data.csv', 'w', newline='') as f:
        config.TRAINING_DATA.to_csv(f)
    # print statements are mostly just for sanity check
    print(str(config.TRAINING_DATA.shape[0]) + " rows in training data.")
    print(str(config.TEST_DATA.shape[0]) + " rows in test data.")
    return 