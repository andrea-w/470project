import pandas as pd
from src.ga.random.initialization import *

NUM_CANDIDATES_PER_GENERATION = 100

def perform_ga_rand_init(data):
    # gen variable tracks which generation (iteration) currently on
    gen = 0
    # create empty dataframe with just the labels from data
    candidates_df = pd.DataFrame(index=data.columns)
    # initialize {NUM_CANDIDATES_PER_GENERATION} random candidates
    for i in range(NUM_CANDIDATES_PER_GENERATION):
        # TODO figure out number of genes in genotype
        candidates_df.append(initialization())
    return