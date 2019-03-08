from wrangle import corr_pearson

from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.create_plot import plot_scatter, plot_heatmap
from functions.run_optimize import run_optimize
from functions.data_hdf5 import retrieve_hdf5
from functions.inputs_check import inputs_check


def optimize_process_view(request):

    '''Shows the results once optimize.html input is received.'''

    # clean the inputs
    inputs = clean_inputs(request)

    # get the current dataset
    data = retrieve_hdf5('dataframe')

    # get the name of the label column
    label_columns = inputs_check({})['label_column']

    # get the name/s of the prediction columns
    pred_cols = data.iloc[:, 0 - inputs_check({})['last_neuron']:].columns

    # combine the columns to be dropped temporarily
    if isinstance(label_columns, list) is False:
        label_columns = [label_columns]
    cols = list(pred_cols) + label_columns

    # create x and y data for optimize
    x = data.drop(cols, 1).values
    y = data[label_columns].values

    # run Talos hyperparemeter optimization
    results = run_optimize(x, y,
                           grid_downsample=inputs['grid_downsample'],
                           epochs=inputs['epochs'])

    # remove columns that have a single unique value
    for col in results:
        if len(results[col].unique()) == 1:
            results.drop(col, 1, inplace=True)

    # prepare data for the contour/heatmap plot
    contour_data = corr_pearson(results)
    z = contour_data.values
    labels = contour_data.columns

    # create the plots
    plot_optimize_contour = plot_heatmap(z, labels, labels)
    plot_optimize = plot_scatter(results['val_acc'].values, results['val_loss'].values)

    return render_template('optimize_result.html',
                           plot_optimize=plot_optimize,
                           plot_optimize_contour=plot_optimize_contour,
                           html_source=results.to_html(classes='table table-striped table-bordered" id="data_frame'))
