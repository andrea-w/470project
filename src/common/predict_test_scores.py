import pandas as pd
import config
import sys

"""
Creates and returns a "predicted_scores_df" pandas dataframe, consisting of
the predicted average test score for 1 of 4 possible tests and the absolute error
of the predicted score vs the actual score for a given (state,year).
A candidate's weights are dot-producted with the relevant data for given (state,year),
which produces one predicted average test score. The script then compares the predicted
avg test score to the 4 actual test scores for the (state,year), and returns
the name of the test that the prediction was nearest to, as well as the absolute error
between the predicted score and the actual test score.
"""
def predict_test_scores(candidates_df):
    predicted_scores_df = pd.DataFrame(columns=['candidate_id','(state,year)','PREDICTED-AVG-SCORE', 'TEST-NAME', 'ABSOLUTE-ERROR'])

    # create list of column labels that are in both candidate dataframe and training_data dataframe
    common_labels = list(set(config.CANDIDATE_COLUMNS_OF_INTEREST).intersection(config.COLUMNS_OF_INTEREST_DATA))
    # make copy of training_data dataframe that only consists of common_labels
    trimmed_data_df = config.TRAINING_DATA[common_labels].copy()

    # iterate through all rows in training_data for each candidate
    # calculating predicted test score for each (state,year) and finding closest test_name and error
    # store results in a new pandas Series, add the new Series object to list_to_append
    # all series will be concatenated to predicted_scores_df at end of loop, since this is computationally quicker
    # than appending one-by-one (as per Pandas documentation)
    list_of_dfs = []
    for c in range(1,config.NUM_CANDIDATES_PER_GENERATION + 1):
        list_of_states_for_candidate = []
        for i, row in trimmed_data_df.iterrows():
            prediction = calculate_test_score_for_one_candidate_and_pk(candidates_df[str(c)], row)
            mse, test_name = find_nearest_test_score(prediction, config.TRAINING_DATA.loc[[row.name], config.TEST_SCORES_COLUMNS])
            s = pd.DataFrame(data={'candidate_id': str(c),'PRIMARY-KEY': row.name,'PREDICTED-SCORE':prediction, 'TEST-NAME':test_name, 'MEAN-SQUARE-ERROR':mse}, index=[row.name])
            list_of_states_for_candidate.append(s)
        candidate_df = pd.concat(list_of_states_for_candidate)
        list_of_dfs.append(candidate_df)

    predicted_scores_df = pd.concat(list_of_dfs)
    predicted_scores_df.set_index(['candidate_id'], inplace=True)

    # TODO delete later
    with open('predicted_scores.csv', 'w', newline='') as f:
        predicted_scores_df.to_csv(f)

    return predicted_scores_df

# calculates estimated test score for given state and year (pk)
# by multiplying candidate's weights with values in pk's row from TRAINING_DATA
# Compares value of predicted score to config.MIN_TEST_SCORE and
# config.MAX_TEST_SCORE. If predicted score outside range, pred_score
# will be reassigned to either MIN_TEST_SCORE or MAX_TEST_SCORE (whichever is closest).
# @params:      candidate       pandas series of labelled weights
def calculate_test_score_for_one_candidate_and_pk(candidate, data_row):
    pred_score = data_row.dot(candidate)

    if pred_score < config.MIN_TEST_SCORE:
            pred_score = config.MIN_TEST_SCORE
    elif pred_score > config.MAX_TEST_SCORE:
            pred_score = config.MAX_TEST_SCORE
    return pred_score

# @params:      prediction - the value of the predicted test score
#               test_scores - pandas series of the 4 test scores
# compares prediction to 4 actual test scores among given training_data entry
# finds nearest actual test score and returns the name of the test
def find_nearest_test_score(prediction, test_scores):
    label = ''
    diff = 9999999999999999
    mse = 9999999999999999
    for index,val in test_scores.items():
        actual_score = val.iloc[0]
        if (abs(actual_score-prediction) < diff):
            diff = abs(actual_score-prediction)
            # calculate Mean Square Error of difference
            mse = diff ** 2
            label = index
    return (mse, label)