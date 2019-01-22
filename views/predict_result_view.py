import pandas as pd
from keras import backend as K

from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.create_plot import plot_histogram
from functions.cache_model import activate_model


def predict_result_view(request):

	inputs = clean_inputs(request)
	data = pd.read_csv(inputs['data'])
	x = data.drop('Outcome', 1).values

	K.clear_session()
	model = activate_model('model.studio.temp')
	probabilities = model.predict(x)
	predictions = model.predict_classes(x)

	if inputs['id_column'] == 'None':
		ids = list(range(len(predictions)))
		inputs['id_column'] = 'ID'
	else:
		ids = data[inputs['id_column']]

	out = pd.DataFrame({
		inputs['id_column']: ids,
		'predictions': [i[0] for i in predictions],
		'probabilities': [round(i[0], 2) for i in probabilities]})

	plot_pred = plot_histogram([i[0] for i in probabilities])

	return render_template('predict_result.html',
						   plot_pred=plot_pred,
						   html_source=out.to_html(classes='table table-striped table-bordered" id="data_frame'))