"""
When running script for the first time on a machine,
first execute in terminal (from root of project directory):
pip install -r requirements.txt
"""

import sys
import time
import config
import sgd.main as sgd
import common.normalization_dim_reduction as ndr
import common.preprocess as preprocess
import ga.random.main as rand_main
import pandas as pd


def main():
    data = preprocess.load_data_file(sys.argv[1])
    # add additional columns to dataframe representing normalized values
    data = ndr.normalize_all(data)
    preprocess.split_into_training_and_test(data)

    start_time = time.time()
    rand_main.perform_ga_rand_init()
    end_time = time.time()
    print('Genetic Algorithm with random init took ' + str(end_time - start_time) + ' seconds.')
    start_time = time.time()
    sgd.perform_sgd()
    end_time = time.time()
    print('SGD took ' + str(end_time - start_time) + ' seconds.')

    return

if __name__ == "__main__":
    main()