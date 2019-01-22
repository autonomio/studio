def clean_inputs(r):

	inputs = {}

	for key in r.form.keys():

		if key == 'drop_cols':
			inputs[key] = r.form.getlist('drop_cols')
		else:	
			inputs[key] = r.form[key]


	for key in inputs.keys():
		try:
			if inputs[key].startswith(('0','1','2','3','4','5','6','7','8','9')):
				if '.' in inputs[key]:
					inputs[key] = float(inputs[key])
				else:
					inputs[key] = int(inputs[key])
		except AttributeError:
			pass
			
	return inputs
