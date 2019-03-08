import pandas as pd


def load_data(inputs):

    '''Handles loading data from a file or url'''

    # read the the file (local or url)
    data = pd.read_csv(inputs['data'])

    # separate the data to x and y datasets
    x = data.drop(inputs['label_column'], 1).values
    y = data[inputs['label_column']].values

    return x, y, data
