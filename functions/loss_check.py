from functions.inputs_check import inputs_check


def loss_check():

    pred_type = inputs_check({})['prediction_type']

    if pred_type == 'binary':
        return 'binary_crossentropy'
    elif pred_type == 'multiclass':
        return 'sparse_categorical_crossentropy'
    elif pred_type == 'multilabel':
        return 'categorical_crossentropy'
    elif pred_type == 'continuous':
        return 'mean_absolute_error'
