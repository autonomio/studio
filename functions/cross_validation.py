import numpy as np
from talos.utils.validation_split import kfold
from sklearn.metrics import mean_absolute_error, f1_score


def cross_validation(x, y, inputs, model, folds=5):

    '''Performs cross_validation for n folds'''

    out = []

    # set the mode according to prediction type
    mode = inputs['prediction_type']

    # split the data into folds
    kx, ky = kfold(x, y, folds, True)

    # run the cross-validation
    for i in range(folds):

        # initiate the model
        model._make_predict_function()

        # make predictions
        y_pred = model.predict(kx[i], verbose=0)

        # choose the right type of test
        if mode == 'binary':
            y_pred = y_pred >= .5
            scores = f1_score(y_pred, ky[i], average='binary')

        elif mode == 'multiclass':
            y_pred = y_pred.argmax(axis=-1)
            scores = f1_score(y_pred, ky[i], average='macro')

        if mode == 'multilabel':
            y_pred = model.predict(kx[i]).argmax(axis=1)
            scores = f1_score(y_pred, ky[i].argmax(axis=1), average='macro')

        elif mode == 'continuous':
            y_pred = model.predict(kx[i])
            scores = mean_absolute_error(y_pred, ky[i])

        # add results to the output
        out.append(scores)

    return np.mean(out), np.sum(out), out
