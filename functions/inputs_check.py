import ast


def inputs_check(inputs):

	'''Handles the case where the inputs is not coming 
	from the user input in config view'''

	try:
		inputs['data']
		with open('/tmp/' + 'inputs.studio.txt', 'w') as f:
			f.write(str(inputs))
			f.close()
	except KeyError:
		with open('/tmp/' + 'inputs.studio.txt', 'r') as f:
			s = f.read()
			f.close()
			inputs = ast.literal_eval(s)

	return inputs