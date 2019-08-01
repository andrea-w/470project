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
        candidate_predictions = predicted_scores_df.loc[str(c),:]
        candidate_dict = find_avg_mse_by_test(candidate_predictions)
        s = pd.DataFrame.from_dict(data=candidate_dict)
        list_of_dfs.append(s)
    accuracy_df = pd.concat(list_of_dfs, axis=1)
    accuracy_df.index = ['AVG_MSE_MATH_4_SCORE', 'AVG_MSE_MATH_8_SCORE', 'AVG_MSE_READING_4_SCORE', 'AVG_MSE_READING_8_SCORE']

    # the maximum possible MSE is equal to the square of the range of the test (500)
    max_MSE = 500**2
    # replace all 'NaN's in accuracy_df with max_MSE, since numerical values are needed later
    # and 'NaN' value means that the candidate failed to predict any scores for the selected test type,
    # which can be considered equivalent to the candidate achieving the maximum possible MSE
    accuracy_df.fillna(max_MSE, inplace=True)

    # append column to accuracy_df that is the sum of all columns for each row (summing over column axis)
    sums = pd.DataFrame(data=accuracy_df.sum(axis=1),columns=['SUM-OF-ROW'])
    accuracy_df = accuracy_df.assign(sum_of_row = sums)

    # TODO delete writing to csv file - helpful for debugging
    with open('accuracy.csv', 'w', newline='') as f:
        accuracy_df.to_csv(f)
    return accuracy_df

# calculates the MSE for a given candidate, grouped by test name
# returns a dict where key is the candidate_id, and value is the list of average MSEs
# @params:  candidate_pred_df   - a splice of the predicted_scores_df focused on one candidate
def find_avg_mse_by_test(candidate_pred_df):
    test_names = ['AVG_MATH_4_SCORE', 'AVG_MATH_8_SCORE', 'AVG_READING_4_SCORE', 'AVG_READING_8_SCORE']
    avg_mse = []
    for t in test_names:
        candidate_test_df = candidate_pred_df[candidate_pred_df['TEST-NAME'] == t]
        avg_mse.append(candidate_test_df['MEAN-SQUARE-ERROR'].mean())
    cand_dict = {str(candidate_pred_df.index[0]): avg_mse}
    return cand_dict