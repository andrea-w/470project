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
    # add additional columns to dataframe
    data = ndr.spending_per_student(data)
    data = ndr.instruction_spending_ratio(data)
    data = ndr.support_services_spending_ratio(data)
    data = ndr.capital_expenditure_ratio(data)
    data = ndr.other_expenditure_ratio(data)
    data = ndr.federal_spending_per_student(data)
    data = ndr.state_spending_per_student(data)
    data = ndr.local_spending_per_student(data)
    data = ndr.ratio_budget_spend(data)
    preprocess.split_into_training_and_test(data)

    rand_main.perform_ga_rand_init()

if __name__ == "__main__":
    main()