import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import backend as K


def simple_neural_net(x_train, y_train, x_val, y_val, params):

    '''Creates a Keras model based on inputs. Note that
    certain things can't change here to ensure compatibility
    with Talos hyperparameter optimization.'''

    # clear session to be safe
    K.clear_session()

    # initiate the Keras model
    model = Sequential()

    # create input layer
    model.add(Dense(params['neurons'],
                    input_dim=x_train.shape[1],
                    activation=params['activation']))

    # dropout after input
    model.add(Dropout(params['dropout']))

    # create hidden layers
    for i in range(params['layers']):
        model.add(Dense(params['neurons']))
        model.add(Dropout(params['dropout']))

    # output layer
    model.add(Dense(params['last_neuron'],
                    activation=params['last_activation']))

    # compile the model
    model.compile(optimizer=params['optimizer'],
                  loss=params['losses'],
                  metrics=[params['metric']])

    # fit the model
    history = model.fit(x=x_train, y=y_train,
                        validation_split=params['validation_split'],
                        batch_size=params['batch_size'],
                        epochs=params['epochs'])

    return history, model
