"""
When running script for the first time on a machine,
first execute in terminal (from root of project directory):
pip install -r requirements.txt
"""

import sys
import config
import common.normalization_dim_reduction as ndr
import common.preprocess as preprocess
import ga.random.main as rand_main
import pandas as pd


def main():
    data = preprocess.load_data_file(sys.argv[1])
    # add additional columns to dataframe representing normalized values
    data = ndr.normalize_all(data)
    preprocess.split_into_training_and_test(data)

    rand_main.perform_ga_rand_init()

if __name__ == "__main__":
    main()