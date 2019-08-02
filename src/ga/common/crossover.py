"""
Performs crossover (reproduction) of parent candidates to produce
{config.NUM_OF_CANDIDATES_PER_GENERATION} children.
Population model is complete replacement, so all parent candidates are replaced by children.
Candidates with higher accuracy scores (fitness function value) are more likely to reproduce than candidates
with low accuracy scores.
"""

import pandas as pd
import numpy as np
import random
import config
import sys

# @params:      candidates_df   pandas DataFrame of parent candidates
#               accuracy_df     pandas DataFrame of parent candidates ordered by decreasing fitness
def set_up_roulette_wheel(candidates_df, accuracy_df):
    # create array of probability cutoffs for each candidate based on their fitness
    # using numpy array instead of pandas dataframe for better performance
    prev_prob = 0.0
    prob_cutoffs = []
    columns = list(accuracy_df)
    # remove last column from list since it's the sum of the rows, not a candidate
    columns.pop()
    accuracy_df_indices = ['AVG_MSE_MATH_4_SCORE', 'AVG_MSE_MATH_8_SCORE', 'AVG_MSE_READING_4_SCORE', 'AVG_MSE_READING_8_SCORE']

    # store all child candidates generated (each is a pandas Series) in a list for later concatenation
    list_of_children = []

    # for each type of test
    for j in accuracy_df_indices:
        # for each candidate
        for i in columns:
            # calculate the candidate's upper bound on probability value and add to list
            prob_val = prev_prob + (accuracy_df.loc[j,i]/accuracy_df.loc[j,'sum_of_row'])
            prob_cutoffs.append(prob_val)
            prev_prob = prob_val
        # create numpy array from list of probability bounds
        prob_cutoffs_array = np.array(prob_cutoffs)
        # reset prev_prob for next iteration
        prev_prob = 0.0
        # reset prob_cutoffs for next iteration
        prob_cutoffs.clear()

        # create 25 children for each type of test
        for y in range(int(config.NUM_CANDIDATES_PER_GENERATION / 4)):     
            child_candidate = roulette_wheel_selection(candidates_df, prob_cutoffs_array)   
            list_of_children.append(child_candidate)
        
    children_candidates_df = pd.concat(list_of_children, axis=1)
    children_candidates_df.columns = [str(i) for i in range(1, config.NUM_CANDIDATES_PER_GENERATION + 1)]
    return children_candidates_df

def roulette_wheel_selection(candidates_df, prob_cutoffs_array):
    # TODO delete writing to csv file - helpful for debugging
    with open('candidates.csv', 'w', newline='') as f:
        candidates_df.to_csv(f)

    # select 2 random float values that will be used to select the 2 parent candidates
    rand_float_1 = random.random()
    rand_float_2 = random.random()

    # find the candidate that corresponds to the rand_float slots on roulette wheel
    prev_val = 0.0
    parent1, parent2 = -1, -1
    for x in range(len(prob_cutoffs_array)): 
        if (prev_val < rand_float_1) and (prob_cutoffs_array[x] > rand_float_1):
            parent1 = x + 1
            break
        else:
            prev_val = prob_cutoffs_array[x]
    prev_val = 0.0
    for x in range(len(prob_cutoffs_array)):
        if (prev_val < rand_float_2) and (prob_cutoffs_array[x] > rand_float_2):
            parent2 = x + 1
            break
        else:
            prev_val = prob_cutoffs_array[x]

    child_candidate = create_offspring(candidates_df[str(parent1)], candidates_df[str(parent2)])

    return child_candidate

# Creates and returns 1 child candidate, given 2 parent candidates
# Crossover is performed after a randomly selected index in the array of candidate genes
# @params:      parent1_candidate    pandas Series containing genotype of first parent    (order does not matter)
#               parent2_candidate    pandas Series containing genotype of second parent   (order does not matter)
def create_offspring(parent1_candidate, parent2_candidate):
    num_features = len(parent1_candidate)
    crossover_point = random.randint(0,num_features-1)
    first_part = pd.Series(parent1_candidate.iloc[:crossover_point+1])
    second_part = pd.Series(parent2_candidate.iloc[crossover_point+1:])
    child_candidate = pd.Series(data=pd.concat([first_part,second_part]))
    if child_candidate.isnull().any().any():
        print(first_part)
        print(second_part)
        print(child_candidate)
        sys.exit()
    return child_candidate