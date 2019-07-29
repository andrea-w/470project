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