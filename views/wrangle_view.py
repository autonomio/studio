from flask import render_template
from functions.data_hdf5 import retrieve_hdf5


def wrangle_view():

    '''Create the initial view for wrangle'''

    data = retrieve_hdf5('dataframe')
    return render_template('wrangle.html', columns=list(data.columns))
