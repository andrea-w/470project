"""
This file is used to store global variables so that they can be shared across modules.
This is based on Python's documentation for recommended best practices.
https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
"""
import pandas as pd

# list of labels in dataframe that are important for data analysis
# (and therefore should have weights assigned to them)
# possible TODO - normalize avg test scores
COLUMNS_OF_INTEREST_DATA = ['STATE', 'YEAR', 'Spend_per_Student', 'Instruction_Spending_Ratio', 'Support_Services_Spending_Ratio', 'Capital_Expenditure_Ratio', 'Other_Expenditure_Ratio', 'Federal_Spending_per_Student',
                       'State_Spending_per_Student', 'Local_Spending_per_Student', 'Ratio_Budget_Spent', 'PreK_RATIO', 'Kinderg_RATIO', 'Grade_4_RATIO', 'Grade_8_RATIO', 'Grade_12_RATIO', 'Primary_RATIO', 'Secondary_RATIO']
CANDIDATE_COLUMNS_OF_INTEREST = COLUMNS_OF_INTEREST_DATA.copy()
CANDIDATE_COLUMNS_OF_INTEREST.remove('STATE')
TEST_SCORES_COLUMNS = ['AVG_MATH_4_SCORE', 'AVG_MATH_8_SCORE', 'AVG_READING_4_SCORE', 'AVG_READING_8_SCORE']

# standardized test scores marked on range [0, 500] according to government website
MIN_TEST_SCORE = 0
MAX_TEST_SCORE = 500

NUM_CANDIDATES_PER_GENERATION = 100
NUM_GENERATIONS = 10

# initialize empty pandas dataframes that will be used across modules
TRAINING_DATA = pd.DataFrame()
TEST_DATA = pd.DataFrame()

print("Config has been set.")
