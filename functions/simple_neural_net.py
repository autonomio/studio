import pandas as pd

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import backend as K


def simple_neural_net(x_train, y_train, x_val, y_val, params):

	K.clear_session()

	model = Sequential() # create model

	model.add(Dense(params['neurons'], input_dim=x_train.shape[1], activation=params['activation'])) # first layer 
	model.add(Dropout(params['dropout']))
	
	for i in range(params['layers']): # hidden layers
		
		model.add(Dense(params['neurons'])) 
		model.add(Dropout(params['dropout']))
	
	model.add(Dense(1, activation=params['last_activation'])) # last layer

	model.compile(optimizer=params['optimizer'],
				  loss=params['losses'],
				  metrics=[params['metric']])

	history = model.fit(x=x_train, y=y_train,
					    validation_split=params['validation_split'],
					    batch_size=params['batch_size'],
					    epochs=params['epochs'])

	return history, model



	