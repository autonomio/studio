def default_params():

	p = {'neurons': [8, 16, 32, 64, 128, 256],
		 'dropout': [0.1, 0.2, 0.3, 0.4, 0.5],
		 'batch_size': [5, 10, 20, 40, 80],
		 'layers': [1, 2, 3, 4, 5],
		 'activation': ['relu','elu'],
		 'last_activation': ['sigmoid'],
		 'optimizer': ['Nadam', 'Adam'],
		 'losses': ['binary_crossentropy'],
		 'metric': ['acc'],
		 'validation_split': [0.3],
		 'epochs': [50]}

	return p