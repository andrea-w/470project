"""
Creates new pandas DataFrame for each candidate, consisting of candidate's id and 
the candidate's Mean Squared Error (MSE) in predicting test scores. 
The fitness function consists of Mean Squared Error values in candidate's accuracy
in predicting scores. An additional column is inserted into the DataFrame with the
normalized MSE for each candidate, for use in determining probability and pairing for
reproduction.
"""

import pandas as pd
import config

# creates a new dataframe to store the fitness function value for each candidate genotype
# compared to the actual test scores for the PK (state,year)
def calculate_accuracy(predicted_scores_df):
    accuracy_df = pd.DataFrame(columns=['TEST-NAME','MSE','NORMALIZED-MSE'])
    list_of_dfs = []
    #for c in range(1, config.NUM_CANDIDATES_PER_GENERATION + 1):
        
    return accuracy_df

# returns the Mean Squared Error for a pandas Series of predicted test scores
# against the Series of the actual test scores
def calculate_MSE(actual_scores, predicted_scores):
    # first perform error checking
    if (actual_scores.len() != predicted_scores.len()):
        return "Error. Mismatch in length of arraylists of scores"
    N = actual_scores.len()
    squared_error = 0
    for i in range(N):
        squared_error += (actual_scores[i] - predicted_scores[i])**2
    # return average squared error
    return squared_error/N