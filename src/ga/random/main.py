import pandas as pd
import numpy as np
import ga.random.initialization as rand_init
import common.calculate_accuracy as ca
import ga.common.encode_genotype as encode
import ga.common.crossover as crossover
from common.predict_test_scores import predict_test_scores
import config
import time


def perform_ga_rand_init():
    # create empty dataframe with just the labels from data
    candidates_df = pd.DataFrame(index=config.CANDIDATE_COLUMNS_OF_INTEREST, columns=[str(c) for c in range(1,config.NUM_CANDIDATES_PER_GENERATION + 1)])

    # initialize {NUM_CANDIDATES_PER_GENERATION} random candidates
    list_of_candidates = list()
    for i in range(config.NUM_CANDIDATES_PER_GENERATION):
        s = encode.encode_genotype(config.CANDIDATE_COLUMNS_OF_INTEREST, rand_init.initialization(len(config.CANDIDATE_COLUMNS_OF_INTEREST)), str(i+1))
        list_of_candidates.append(s)
    candidates_df = pd.concat(list_of_candidates, axis=1)

    print('initial (random) candidates:')
    print(candidates_df)

    for g in range(config.NUM_GENERATIONS - 1):
        start_time = time.time()
        predicted_df = predict_test_scores(candidates_df) 
        end_time = time.time()
        print("\n\ntime elapsed to complete 1 iteration of predictions: " + str(end_time - start_time))
        accuracy_df = ca.calculate_accuracy(predicted_df)
        candidates_df = crossover.set_up_roulette_wheel(candidates_df, accuracy_df)

    # TODO delete writing to csv file - helpful for debugging
    with open('children.csv', 'w', newline='') as f:
        candidates_df.to_csv(f)

    return

