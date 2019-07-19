import pandas as pd 
import numpy as np

"""
Creates a pandas Series (1-dimensional column with labels)
to represent a candidate genotype
Takes pandas dataframe as @param
"""
def encode_genotype(dataframe):
    # get list of column labels from dataframe of imported CSV file
    labels = [dataframe.columns]
    # TODO set values for weights of features - may be random or may be set
    data = np.array([])

    s = pd.Series(data, index=labels)
    return s
