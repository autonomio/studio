from functions.inputs_check import inputs_check


def last_activation_check():

    pred_type = inputs_check({})['prediction_type']

    if pred_type == 'binary':
        return 'sigmoid'
    elif pred_type == 'multiclass':
        return 'softmax'
    elif pred_type == 'multilabel':
        return 'softmax'
    elif pred_type == 'continuous':
        return None
