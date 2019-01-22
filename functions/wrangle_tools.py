import warnings

import numpy as np
from wrangle.rescale import mean_zero
from wrangle.outliers import outliers
from wrangle.to_multiclass import to_multiclass
from wrangle.to_multilabel import to_multilabel


def _handle_commas(data, replace_with):

    for col in data.columns:
        try:
            data[col] = data[col].str.replace(',', replace_with)
        except AttributeError:
            pass

    return data

def drop_cols(data, cols):
    return data.drop(cols, 1)

def drop_nan_cols(data):
    return data.dropna(axis=1, thresh=len(data) * 0.9)

def drop_nan_rows(data):
    return data.dropna()
    
def drop_nonnumeric(data):
    return data._get_numeric_data()

def drop_duplicate_rows(data):
    return data.drop_duplicates()
    
def remove_commas(data):
    return _handle_commas(data, '')

def replace_commas(data):
    return _handle_commas(data, '.')

def convert_to_floats(data):
    return data.astype(float)

def transform_meanzero(data):
    return mean_zero(data)

def transform_log(data):
    return data.apply(np.log1p)

def transform_sqrt(data):
    return data.apply(np.sqrt)

def remove_outliers(data):
    warnings.simplefilter('ignore')
    for col in data.columns:
        data = outliers(data, col)
    return data