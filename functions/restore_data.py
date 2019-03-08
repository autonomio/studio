from functions.data_hdf5 import retrieve_hdf5
from functions.inputs_check import inputs_check


def restore_data():

    data = retrieve_hdf5('dataframe')

    # get the name of the label column
    label_columns = inputs_check({})['label_column']

    # get the name/s of the prediction columns
    pred_cols = inputs_check({})['pred_cols']

    # combine the columns to be dropped temporarily
    if isinstance(label_columns, list) is False:
        label_columns = [label_columns]
    cols = list(pred_cols) + label_columns

    x = data.drop(cols, 1).values
    y = data[label_columns].values

    return x, y, data
