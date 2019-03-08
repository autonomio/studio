import pandas as pd

from flask import render_template
from keras import backend as K

from functions.simple_neural_net import simple_neural_net
from functions.clean_inputs import clean_inputs
from functions.cross_validation import cross_validation
from functions.create_plot import create_plots
from functions.data_hdf5 import store_hdf5
from functions.inputs_check import inputs_check
from functions.cache_model import save_model_as
from functions.load_data import load_data
from functions.get_last_neuron import get_last_neuron
from functions.restore_data import restore_data


def training_view(request):

    '''This view handles everything related with training
    for both first time training after inputs and consequent ones.

    Takes it's input from '/' i.e. studio.html and loads from cache
    as required for consequent uses.

    request : flask post request

    '''

    # C O N N E C T I O N
    inputs = clean_inputs(request)

    # handle the case where inputs are already in
    inputs = inputs_check(inputs)

    # load the data for the new input case
    referrer = request.headers.get("Referer")
    refs = ['http://127.0.0.1:5000/training', 'http://127.0.0.1:5000/']

    if referrer in refs:
        x, y, data = load_data(inputs)

    # load the data for all other cases
    else:
        x, y, data = restore_data()

    # calculate last neuron count
    inputs = get_last_neuron(y, inputs)

    K.clear_session()
    # create and train the model (same model goes to optimize)
    history, model = simple_neural_net(x, y, None, None, params=inputs)

    # add the predictions to the dataframe
    preds = pd.DataFrame(model.predict(x))
    preds.columns = ['pred_' + str(i) for i in range(len(preds.columns))]
    try:
        data.drop(preds.columns, 1, inplace=True)
    except KeyError:
        pass
    data = data.merge(preds,
                      left_index=True,
                      right_index=True)

    # store the dataframe and model
    save_model_as(model, 'model.studio.temp')
    store_hdf5(data, 'dataframe')

    # perform cross-validation
    score_mean, score_std, validated = cross_validation(x, y, inputs, model)

    # separate the prediction column/s
    preds = data.iloc[:, 0 - inputs['last_neuron']:]

    # create the plots
    cross_val, train, train_val, predictions = create_plots(validated,
                                                            history,
                                                            preds)

    # R E N D E R  P A G E
    return render_template('training.html',
                           plot_cross_val=cross_val,
                           plot_train=train,
                           plot_train_val=train_val,
                           plot_predictions=predictions)
