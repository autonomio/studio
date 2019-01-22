from flask import redirect
from functions.data_hdf5 import retrieve_hdf5, store_hdf5


def wrangle_save_view():

		data = retrieve_hdf5('dataframe_temp')
		store_hdf5(data, 'dataframe')

		return redirect("/dataframe")