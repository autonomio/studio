import numpy as np
from functions.inputs_check import inputs_check


def get_last_neuron(y, inputs):

    '''Infers the last_neuron count based on the type of prediction
    task in question.'''

    # get uniques for multiclass case
    if inputs['prediction_type'] == 'multiclass':
        inputs['last_neuron'] = len(np.unique(y))
        inputs['pred_cols'] = np.unique(y).tolist()

    # get dimensions for multilabel
    elif inputs['prediction_type'] == 'multilabel':
        inputs['last_neuron'] = y.shape[1]
        inputs['pred_cols'] = list(range(y.shape[1]))

    # assume as one for both binary and continuous cases
    else:
        inputs['last_neuron'] = 1
        inputs['pred_cols'] = [0]

    inputs['pred_cols'] = ['pred_' + str(i) for i in inputs['pred_cols']]
    inputs = inputs_check(inputs)

    return inputs
