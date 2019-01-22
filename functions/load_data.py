import pandas as pd


def load_data(inputs):
		
	data = pd.read_csv(inputs['data'])
	x = data.drop(inputs['label_column'], 1).values 
	y = data[inputs['label_column']].values

	return x, y, data