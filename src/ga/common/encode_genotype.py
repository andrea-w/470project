import pandas as pd 
import numpy as np

"""
Creates a pandas Series (1-dimensional column with labels)
to represent a candidate genotype
Takes list of column labels as @param
and list of weights (values) as second @param
"""
def encode_genotype(labels, values, name):
    # set values for weights of features - may be random or may be set
    data = np.array(values)

    s = pd.Series(data, index=labels, name=name)
    s = s.fillna(0)
    return s
