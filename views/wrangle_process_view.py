from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.data_hdf5 import retrieve_hdf5, store_hdf5
from functions.inputs_check import inputs_check
import functions.wrangle_tools as wrangle_tools


def wrangle_process_view(request):

    # get the inputs from wrangle.html
    inputs = clean_inputs(request)

    # get the current version of input data
    data = retrieve_hdf5('dataframe')

    # get the name of the label column
    label_columns = inputs_check({})['label_column']

    # get the name/s of the prediction columns
    pred_cols = data.iloc[:, 0 - inputs_check({})['last_neuron']:].columns

    # combine the columns to be dropped temporarily
    if isinstance(label_columns, list) is False:
        label_columns = [label_columns]
    cols = list(pred_cols) + label_columns

    # remove prediction and label columns temporarily
    data_temp = data[cols]
    data.drop(cols, 1, inplace=True)

    # handle the user inputs for data transformation
    for key in inputs:
        if inputs[key] not in ['False', []]:
            if key == 'drop_cols':
                data = wrangle_tools.__getattribute__(key)(data, inputs[key])
            elif key == 'transformation':
                data = wrangle_tools.__getattribute__(inputs[key])(data)
            else:
                data = wrangle_tools.__getattribute__(key)(data)

    # join back the prediction and label columns
    data = data.merge(data_temp, left_index=True, right_index=True)

    # store a temporary file pending user confirmation to save
    store_hdf5(data, 'dataframe_temp')

    # the needed class string for dataTables to work correctly
    css_class = 'table table-striped table-bordered" id="data_frame'

    return render_template('wrangle_process.html',
                           html_source=data.to_html(classes=css_class))
