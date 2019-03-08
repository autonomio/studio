from flask import redirect
from functions.data_hdf5 import retrieve_hdf5, store_hdf5


def wrangle_save_view():

    '''Handles the wrangle_process_view.html request to
    save the changes to the dataframe.'''

    # load the temporarily saved version of the data
    data = retrieve_hdf5('dataframe_temp')

    # then replace the original input version
    store_hdf5(data, 'dataframe')

    # redirect to dataframe view so user gets visual confirmation of change
    return redirect("/dataframe")
