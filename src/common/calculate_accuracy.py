"""
Creates new pandas DataFrame for each candidate, consisting of candidate's id and 
the candidate's Mean Squared Error (MSE) in predicting test scores. 
The fitness function consists of Mean Squared Error values in candidate's accuracy
in predicting scores. An additional column is inserted into the DataFrame with the
normalized MSE for each candidate, for use in determining probability and pairing for
reproduction.
"""

import pandas as pd
import math
import config

# creates a new dataframe to store the fitness function value for each candidate genotype
# compared to the actual test scores for the PK (state,year)
def calculate_accuracy(predicted_scores_df):
    list_of_dfs = []
    for c in range(1, config.NUM_CANDIDATES_PER_GENERATION + 1):
        candidate_predictions = predicted_scores_df.loc[str(c)]
        avg_mse = find_avg_mse_by_test(candidate_predictions)
        s = pd.Series(data=avg_mse,name=str(c))
        list_of_dfs.append(s)
    accuracy_df = pd.concat(list_of_dfs,keys=[str(c) for c in range(1, config.NUM_CANDIDATES_PER_GENERATION + 1)])
    # TODO delete later
    print('ACCURACY DATAFRAME:')
    print(accuracy_df)
    return accuracy_df

# calculates the MSE for a given candidate, grouped by test name
# returns a dict (of size 4) where key is the test name, and value is the average MSE
# @params:  candidate_pred_df   - a splice of the predicted_scores_df focused on one candidate
def find_avg_mse_by_test(candidate_pred_df):
    test_names = ['AVG_MATH_4_SCORE', 'AVG_MATH_8_SCORE', 'AVG_READING_4_SCORE', 'AVG_READING_8_SCORE']
    # the maximum possible MSE is equal to the square of the range of the test (500)
    max_MSE = 500**2
    avg_mse = {}
    for t in test_names:
        candidate_test_df = candidate_pred_df[candidate_pred_df['TEST-NAME'] == t]
        avg_mse[t+'_MSE'] = candidate_test_df['MEAN-SQUARE-ERROR'].mean()
    # replace any NaN values in avg_mse dict with max_MSE, since we later need numerical values for
    # all average MSEs, and if a candidate has not predicted a single score for a certain type of test,
    # that candidate can be considered to have made the maximum possible MSE for that test type
    for k,v in avg_mse.items():
        if math.isnan(v):
            avg_mse[k] = max_MSE
    return avg_mse