import sys
from src.common.normalization_dim_reduction import *
from src.common.preprocess import *
from src.ga.random.main import *

def main():
    data = load_data_file(sys.argv[1])
    print("Dataframe has " + str(data.shape[1]) + " columns.")
    # add additional columns to dataframe
    data = spending_per_student(data)
    data = instruction_spending_ratio(data)
    data = support_services_spending_ratio(data)
    data = capital_expenditure_ratio(data)
    data = other_expenditure_ratio(data)
    data = federal_spending_per_student(data)
    data = state_spending_per_student(data)
    data = local_spending_per_student(data)
    data = ratio_budget_spend(data)
    print("Modified dataframe has " + str(data.shape[1]) + " columns.")
    print("There should be 9 additional columns.")
    training_data, test_data = split_into_training_and_test(data)

    perform_ga_rand_init(training_data)

if __name__ == "__main__":
    main()