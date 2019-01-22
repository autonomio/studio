from flask import render_template
from functions.data_hdf5 import retrieve_hdf5

def dataframe_view():

	data = retrieve_hdf5('dataframe')
	return render_template('dataframe.html',
						   html_source=data.to_html(classes='table table-striped table-bordered" id="data_frame'))
