from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.data_hdf5 import retrieve_hdf5, store_hdf5
from functions.inputs_check import inputs_check
import functions.wrangle_tools as wrangle_tools

def wrangle_process_view(request):

	inputs = clean_inputs(request)

	data = retrieve_hdf5('dataframe')

	label_column = inputs_check({})['label_column']
	cols = [label_column] + ['studio_predictions']

	data_temp = data[cols]
	data.drop(cols, 1, inplace=True)

	for key in inputs:
		if inputs[key] not in ['False', []]:
			if key == 'drop_cols':
				data = wrangle_tools.__getattribute__(key)(data, inputs[key])
			elif key == 'transformation':
				data = wrangle_tools.__getattribute__(inputs[key])(data)
			else:
				data = wrangle_tools.__getattribute__(key)(data)

	data = data.merge(data_temp, left_index=True, right_index=True)

	store_hdf5(data, 'dataframe_temp')

	return render_template('wrangle_process.html',
							html_source=data.to_html(classes='table table-striped table-bordered" id="data_frame'))
