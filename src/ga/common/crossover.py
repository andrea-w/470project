"""
Performs crossover (reproduction) of parent candidates to produce
{config.NUM_OF_CANDIDATES_PER_GENERATION} children.
Population model is complete replacement, so all parent candidates are replaced by children.
Candidates with higher accuracy scores (fitness function value) are more likely to reproduce than candidates
with low accuracy scores.
"""

import pandas as pd

# @params:      candidates_df   pandas DataFrame of parent candidates
#               accuracy_df     pandas DataFrame of parent candidates ordered by decreasing fitness
def perform_crossover(candidates_df, accuracy_df):
    return

def roulette_wheel_selection(accuracy_df):
    # create dictionary of summed MSEs for each test type from accuracy_df
    test_MSE_sums = {}
    unique_test_names = accuracy_df.iloc[1].unique().tolist()
    for t in unique_test_names:
        test_MSE_sums[t] = accuracy_df[accuracy_df.iloc[0] == t].sum()
    print('test_mse_sums')
    print(test_MSE_sums)
    return