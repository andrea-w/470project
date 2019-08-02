import json
import fnv
import numpy as np 
import pandas as pd
import random
import codecs
import config
from math import sqrt
from collections import OrderedDict

# =============== Global Variables ==================
BATCH_SIZE = 2
EPOCHS = 100
LEARNING_RATE = 0.0001
RELEVANT_FEATURES = ['YEAR','Spend_per_Student', 'Instruction_Spending_Ratio', 'Support_Services_Spending_Ratio', 'Capital_Expenditure_Ratio', 'Other_Expenditure_Ratio', 'Federal_Spending_per_Student', 'State_Spending_per_Student', 'Local_Spending_per_Student', 'Ratio_Budget_Spent', 'PreK_RATIO', 'Kinderg_RATIO', 'Grade_4_RATIO', 'Grade_8_RATIO', 'Grade_12_RATIO', 'Primary_RATIO', 'Secondary_RATIO']
TEST_SCORE_COLUMN_LABELS = ['AVG_MATH_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_4_SCORE','AVG_READING_8_SCORE']
# ===================================================

# ================ Function Definitions ==============
# https://machinelearningmastery.com/implement-linear-regression-stochastic-gradient-descent-scratch-python/

# perform mean normalization on training data
# @param:   df      pandas DataFrame of data to normalize
def normalize_data(df):
    normalized_df = (df - df.mean())/df.std()
    return normalized_df

# perform test on test data
def test_coefficients(df, coeffs):
    errors = list()
    actual_scores = df[TEST_SCORE_COLUMN_LABELS]
    df = df.drop(columns=TEST_SCORE_COLUMN_LABELS)
    counter = 0
    for index, row in df.iterrows():
        predicted_score = coeffs.dot(row)
        for test_name in TEST_SCORE_COLUMN_LABELS:
            error = abs(actual_scores[test_name] - predicted_score) / actual_scores[test_name]
            errors.append(error)
    return errors

# split the dataset into batches for efficiency
def split_into_batches(data):
    split_dataset = list()
    for x in range(int(data.shape[0]/BATCH_SIZE)):
        split_dataset.append(data.sample(BATCH_SIZE))
    return split_dataset

# predict the coefficients
def predict_coefficients(df, coefficients):
    actual_scores = df[TEST_SCORE_COLUMN_LABELS]
    df = df.drop(columns=TEST_SCORE_COLUMN_LABELS)
    counter = 0
    for index, row in df.iterrows():
        # y_hat is the predicted test score
        y_hat = coefficients.dot(row)
        # FIXME y_hat appears to be outputting a mean normalized value, when I think it should be the absolute value
        # find which actual test score y_hat is closest to
        test_errors = (actual_scores.sub(y_hat[counter])).abs()
        smallest_error = test_errors.min(axis=1)[counter]
        # g is gradient             
        g = row.multiply(smallest_error)
        coefficients = coefficients.add(g.multiply(LEARNING_RATE))
        counter += 1
     
    # we previously removed the test scores from the dataframe because that's the "y"
    # now we have to add it back to the dataframe because it'll be needed again for each epoch
    #df.assign(actual_scores)
    return coefficients

# estimate the linear regression coefficients with SGD
def estimate_sgd_coefficients(training_batches):
    # create list of (float)coefficients for each feature (initialized to 0.0)
    coeffs = pd.DataFrame(np.random.rand(BATCH_SIZE, len(RELEVANT_FEATURES)), columns=RELEVANT_FEATURES)
    for e in range(EPOCHS):
        for batch in training_batches:
            coeffs = predict_coefficients(batch, coeffs)
    return coeffs   

# perform linear regression on the training batches,
# and then test the results against the test batches
def linear_regression(training_batches, test_batches):
    coeffs = estimate_sgd_coefficients(training_batches) 
    # coeffs is an array of arrays of coefficients. We just need the final array
    #coeffs = coeffs[-1]
    print('coeffs: ' + str(coeffs))
    """
    errors = test_coefficients(test_batches, coeffs)
    print('errors: ' + str(errors))

    # output to terminal window results of testing
    accurate = 0
    extra_accurate = 0
    for e in errors:
        if e <= 0.05:
            accurate += 1
        if e <= 0.025:
            extra_accurate += 1
    print("Accurate within 5% {} percent of the time".format(100 * accurate / len(errors))) 
    print("Accurate within 2.5% {} percent of the time".format(100 * extra_accurate / len(errors))) 
    """
    return coeffs

# print the resulting array of coefficients to the specified filepath
def print_to_file(filepath, coeffs):
    with open('sgd_coeffs.csv', 'w', newline='') as f:
        coeffs.to_csv(f)


# ====================== MAIN ===========================
def perform_sgd():
    # normalize training data by column
    # first must make copy of training data and pop 'STATE' column because it has string values
    # so can't be normalized
    training_copy = config.TRAINING_DATA.drop(columns=['STATE'])
    # also drop other columns that are not needed or relevant
    for c in training_copy.columns:
        if c not in RELEVANT_FEATURES and c not in TEST_SCORE_COLUMN_LABELS:
            training_copy = training_copy.drop(columns=[c])
    normalized_training_data = normalize_data(training_copy)

    # note that test data is being normalized against min and max values observed in training data, so
    # it is possible that normalized test data may contain values > 1 or < 0
    test_copy = config.TEST_DATA.drop(columns=['STATE'])
    # also drop other columns that are not relevant
    for c in test_copy.columns:
        if c not in RELEVANT_FEATURES and c not in TEST_SCORE_COLUMN_LABELS:
            test_copy = test_copy.drop(columns=[c])
    normalized_test_data = normalize_data(test_copy)

    training_batches = split_into_batches(normalized_training_data)
    test_batches = split_into_batches(normalized_test_data)

    # this is where the primary computation is done
    coeffs = linear_regression(training_batches, test_batches)

    # print resulting coefficients for each feature to specified file
    print_to_file("output.json", coeffs)

    return coeffs


