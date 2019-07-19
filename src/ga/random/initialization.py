"""
Script to generate random values in range (0,1)
to be used for random initialization of GA candidate
"""

import pandas as pd 
import random

# Returns list of random floats of length @param n
# to be assigned to GA candidate
def initialization(n):
    return list(random.random() for i in range(n))