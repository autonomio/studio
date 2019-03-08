from functions.inputs_check import inputs_check
from functions.loss_check import loss_check
from functions.last_activation_check import last_activation_check


def default_params():

    '''A general exploratory set of parameters'''

    p = {'neurons': [8, 16, 32, 64, 128, 256],
         'dropout': [0.1, 0.2, 0.3, 0.4, 0.5],
         'batch_size': [5, 10, 20, 40, 80],
         'layers': [1, 2, 3, 4, 5],
         'activation': ['relu', 'elu'],
         'last_activation': [last_activation_check()],
         'last_neuron': [inputs_check({})['last_neuron']],
         'optimizer': ['Nadam', 'Adam'],
         'losses': [loss_check()],
         'metric': ['acc'],
         'validation_split': [0.3]}

    return p
