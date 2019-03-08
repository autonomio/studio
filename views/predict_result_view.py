import pandas as pd
from keras import backend as K

from flask import render_template

from functions.clean_inputs import clean_inputs
from functions.create_plot import plot_histogram
from functions.cache_model import activate_model
from functions.inputs_check import inputs_check


def predict_result_view(request):

    '''Takes care of the processing for the inputs that
    that are received through predict.html'''

    inputs = clean_inputs(request)
    data = pd.read_csv(inputs['data'])

    x = data.drop(inputs_check({})['label_column'], 1).values

    K.clear_session()
    model = activate_model('model.studio.temp')
    probabilities = model.predict(x)
    predictions = model.predict_classes(x)

    if inputs['id_column'] is None:
        ids = list(range(len(predictions)))
        inputs['id_column'] = 'ID'
    else:
        ids = data[inputs['id_column']]

    out = pd.DataFrame(probabilities)
    out.columns = inputs_check({})['pred_cols']
    preds = pd.DataFrame(predictions)
    preds.columns = ['class']
    out = out.merge(preds, left_index=True, right_index=True)
    out[inputs['id_column']] = ids

    plot_pred = plot_histogram(pd.DataFrame(probabilities))

    css_class = 'table table-striped table-bordered" id="data_frame'

    return render_template('predict_result.html',
                           plot_pred=plot_pred,
                           html_source=out.to_html(classes=css_class))
