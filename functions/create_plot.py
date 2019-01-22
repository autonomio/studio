import json

import plotly
import plotly.graph_objs as go

import numpy as np
import pandas as pd

colorscale_heat = [[0.0, '#208AAE'],
                   [0.1111111111111111, '#489FBC'],
                   [0.2222222222222222, '#71B4CB'],
                   [0.3333333333333333, '#99C9DA'],
                   [0.4444444444444444, '#C2DFE8'],
                   [0.5555555555555556, '#E7C3BB'],
                   [0.6666666666666666, '#D79C8E'],
                   [0.7777777777777778, '#C77461'],
                   [0.8888888888888888, '#B74D34'],
                   [1.0, '#A72608']]



def create_plots(cross_val, training, preds):

    # CROSS VALIDATION
    
    x = np.array(list(range(len(cross_val))))
    y = np.array(cross_val)

    cross_val = [
        go.Bar(
            x=x,
            y=y,
            name='Cross Validation',
            marker=dict(color='#208AAE')
        )
    ]

    cross_val_json = json.dumps(cross_val, cls=plotly.utils.PlotlyJSONEncoder)

    # PREDICTIONS

    predictions = [go.Histogram(x=preds, name='Predictions', marker=dict(color='#208AAE'))]
    predictions_json = json.dumps(predictions, cls=plotly.utils.PlotlyJSONEncoder)


    # TRAINING VALIDATION
    acc = go.Scatter(x=list(range(len(training.history['acc']))),
                     y=training.history['acc'],
                     name='Accuracy',
                     line = dict(color='#208AAE', width=4)
                     )

    loss = go.Scatter(x=list(range(len(training.history['loss']))),
                      y=training.history['loss'],
                      name='Loss',
                      line = dict(color='#A72608', width=4)
                      )




    train = [acc, loss]
    train_json = json.dumps(train, cls=plotly.utils.PlotlyJSONEncoder)



    # TRAINING VALIDATION
    val_acc = go.Scatter(x=list(range(len(training.history['val_acc']))),
                         y=training.history['val_acc'],
                         name='Validation Accuracy',
                         line = dict(color='#208AAE', width=4)
                         )

    val_loss = go.Scatter(x=list(range(len(training.history['val_loss']))),
                        y=training.history['val_loss'],
                        name='Validation Loss',
                        line = dict(color='#A72608', width=4)
                        )

    train_val = [val_acc, val_loss]
    train_val_json = json.dumps(train_val, cls=plotly.utils.PlotlyJSONEncoder)


    return cross_val_json, train_json, train_val_json, predictions_json


def plot_histogram(preds):

    predictions = [go.Histogram(x=preds, name='Predictions', marker=dict(color='#208AAE'))]
    predictions_json = json.dumps(predictions, cls=plotly.utils.PlotlyJSONEncoder)

    return predictions_json


def plot_scatter(x, y):

    scatter = [go.Scatter(x=x,
                         y=y,
                         name='Validation Results',
                         mode = 'markers',
                         marker=dict(color='#208AAE')
                         )]
    scatter_json = json.dumps(scatter, cls=plotly.utils.PlotlyJSONEncoder)

    return scatter_json


def plot_heatmap(z, x, y):

    heatmap = [go.Heatmap(z=z,
                          x=x,
                          y=y,
                          colorscale=colorscale_heat)]

    heatmap_json = json.dumps(heatmap, cls=plotly.utils.PlotlyJSONEncoder)

    return heatmap_json


def plot_contour(z, x, y):

    countour = [go.Contour(z=z,
                           x=x,
                           y=y,
                           colorscale='Jet')]

    contour_json = json.dumps(countour, cls=plotly.utils.PlotlyJSONEncoder)

    return contour_json
