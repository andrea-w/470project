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
    data = config.TRAINING_DATA
    # create empty dataframe with just the labels from data
    candidates_df = pd.DataFrame(columns=config.CANDIDATE_COLUMNS_OF_INTEREST)

    # initialize {NUM_CANDIDATES_PER_GENERATION} random candidates
    for i in range(config.NUM_CANDIDATES_PER_GENERATION):
        s = encode.encode_genotype(config.CANDIDATE_COLUMNS_OF_INTEREST, rand_init.initialization(len(config.CANDIDATE_COLUMNS_OF_INTEREST)), str(i+1))
        candidates_df = candidates_df.append(s)
    candidates_df.head()

    # TODO delete writing to csv file - helpful for debugging
    with open('candidates.csv', 'w', newline='') as f:
        candidates_df.to_csv(f)

    for g in range(config.NUM_GENERATIONS - 1):
        start_time = time.time()
        predicted_df = predict_test_scores(candidates_df) 
        end_time = time.time()
        print("time elapsed to complete 1 iteration of predictions: " + str(end_time - start_time))
        accuracy_df = ca.calculate_accuracy(predicted_df)
        children_df = crossover.set_up_roulette_wheel(candidates_df, accuracy_df)

    # TODO delete writing to csv file - helpful for debugging
    with open('children.csv', 'w', newline='') as f:
        children_df.to_csv(f)

    return

