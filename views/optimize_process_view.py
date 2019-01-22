import pandas as pd
from keras import backend as K
import wrangle as wrangle
from wrangle import corr_pearson
from wrangle.convert_to_numeric import convert_to_numeric

from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.create_plot import plot_scatter, plot_heatmap
from functions.cache_model import activate_model
from functions.run_optimize import run_optimize
from functions.data_hdf5 import retrieve_hdf5
from functions.inputs_check import inputs_check

def optimize_process_view(request):

	'''Shows the results once optimize.html input is received.'''

	# clean the inputs
	inputs = clean_inputs(request)

	# get the current dataset
	data = retrieve_hdf5('dataframe')

	# load the name of the prediction column
	label_column = inputs_check({})['label_column']
	
	# these will be dropped from x
	cols = [label_column] + ['studio_predictions']

	# create x and y data for optimize
	x = data.drop(cols, 1).values
	y = data[label_column].values

	# run Talos hyperparemeter optimization
	results = run_optimize(x, y, grid_downsample=inputs['grid_downsample'])
	
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