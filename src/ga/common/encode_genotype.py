import pandas as pd 
import numpy as np

"""
Creates a pandas Series (1-dimensional column with labels)
to represent a candidate genotype
"""
def encode_genotype():
    # TODO get list of column labels from dataframe of imported CSV file
    labels = []
    # TODO set values for weights of features - may be random or may be set
    data = np.array([])

    s = pd.Series(data, index=labels)
    return s
