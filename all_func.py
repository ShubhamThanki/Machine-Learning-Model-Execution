import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder , OrdinalEncoder, LabelEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import pickle 
import seaborn as sns
import matplotlib.pyplot as plt




def same(x):
    return x

a = FunctionTransformer(same)