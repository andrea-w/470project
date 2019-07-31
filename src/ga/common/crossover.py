"""
Performs crossover (reproduction) of parent candidates to produce
{config.NUM_OF_CANDIDATES_PER_GENERATION} children.
Population model is complete replacement, so all parent candidates are replaced by children.
Candidates with higher accuracy scores (fitness function value) are more likely to reproduce than candidates
with low accuracy scores.
"""

import pandas as pd
import random

# @params:      candidates_df   pandas DataFrame of parent candidates
#               accuracy_df     pandas DataFrame of parent candidates ordered by decreasing fitness
def perform_crossover(candidates_df, accuracy_df):
    return

def roulette_wheel_selection(accuracy_df):

    return

# Creates and returns 2 child candidates, given 2 parent candidates
# Crossover is performed after a randomly selected index in the array of candidate genes
# @params:      parent1_candidate    pandas Series containing genotype of first parent    (order does not matter)
#               parent2_candidate    pandas Series containing genotype of second parent   (order does not matter)
def create_offspring(parent1_candidate, parent2_candidate):
    num_features = parent1_candidate.shape[1]
    return