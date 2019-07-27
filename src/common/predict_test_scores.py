import pandas as pd
import config

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
    iterables = [[range(1,candidates_df.shape[0])], config.TRAINING_DATA.index]
    index = pd.MultiIndex.from_product(iterables, names=['candidate_id', '(state,year)'])
    predicted_scores_df = pd.DataFrame(index=index, columns=['PREDICTED-AVG-SCORE', 'TEST-NAME', 'ABSOLUTE-ERROR'])

    # create list of column labels that are in both candidate dataframe and training_data dataframe
    common_labels = list(set(config.CANDIDATE_COLUMNS_OF_INTEREST).intersection(config.COLUMNS_OF_INTEREST_DATA))
    # make copy of training_data dataframe that only consists of common_labels
    trimmed_data_df = config.TRAINING_DATA[common_labels].copy()

    for c in range(1,candidates_df.shape[0]):
        for index, row in trimmed_data_df.iterrows():
            prediction = calculate_test_score_for_one_candidate_and_pk(candidates_df.iloc[c], row)
            error, test_name = find_nearest_test_score(prediction, config.TRAINING_DATA.loc[[row.name], config.TEST_SCORES_COLUMNS])
            s = pd.Series(data=[prediction, test_name, error], index=(c,index), name=(c,index))
            predicted_scores_df.append(s)

    return predicted_scores_df

# calculates estimated test score for given state and year (pk)
# by multiplying candidate's weights with values in pk's row from TRAINING_DATA
# @param pk is a string indicating the Primary Key from training_data
# @param candidate is pandas series of labelled weights
def calculate_test_score_for_one_candidate_and_pk(candidate, data_row):
    pred_score = data_row.dot(candidate)
    return pred_score

# @params:      prediction - the value of the predicted test score
#               test_scores - pandas series of the 4 test scores
# compares prediction to 4 actual test scores among given training_data entry
# finds nearest actual test score and returns the name of the test
def find_nearest_test_score(prediction, test_scores):
    label = ''
    diff = 9999999999
    for index,val in test_scores.items():
        actual_score = val.iloc[0]
        if (abs(actual_score-prediction) < diff):
            diff = abs(actual_score-prediction)
            label = index
    return (diff, label)