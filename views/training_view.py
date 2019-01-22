from flask import render_template
from keras import backend as K

from functions.simple_neural_net import simple_neural_net
from functions.clean_inputs import clean_inputs
from functions.cross_validation import cross_validation
from functions.create_plot import create_plots, plot_histogram
from functions.data_hdf5 import store_hdf5
from functions.inputs_check import inputs_check
from functions.cache_model import save_model_as
from functions.load_data import load_data


def training_view(request):

	'''This view handles everything related with training
	for both first time training after inputs and consequent ones. 

	Takes it's input from '/' i.e. studio.html and loads from cache
	as required for consequent uses.

	'''

	# C O N N E C T I O N
	inputs = clean_inputs(request)

	# handle the case where inputs are already in
	inputs = inputs_check(inputs)

	# load the data based on the inputs
	x, y, data = load_data(inputs)

	K.clear_session()
	# create and train the model (same model goes to optimize)
	history, model = simple_neural_net(x, y, None, None, params=inputs)

	# add the predictions to the dataframe
	data['studio_predictions'] = model.predict(x)

	# store the dataframe and model
	save_model_as(model, 'model.studio.temp')
	store_hdf5(data, 'dataframe')

	# perform cross-validation
	score_mean, score_std, validated = cross_validation(inputs, model)

	# create the plots
	cross_val, train, train_val, predictions = create_plots(validated,
											   				history,
											   				data.studio_predictions)

	# R E N D E R  P A G E
	return render_template('training.html',
						   score_mean=score_mean,
						   score_std=score_std,
						   validated=validated,
						   plot_cross_val=cross_val,
						   plot_train=train,
						   plot_train_val=train_val,
						   plot_predictions=predictions)