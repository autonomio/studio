def clean_inputs(r):

    '''Handles the user input from the flask form
    request into a format that makes sense for Keras. The
    idea is (at least for now) to handle inputs from all
    views in this same file.

    TODO: use regex to detect number as the current way
    still allows a case where something starts with a
    number but is not a number actually.
    '''

    inputs = {}

    # create a dictionary out of the inputs
    for key in r.form.keys():

        # handle a list input separately
        if key == 'drop_cols':
            inputs[key] = r.form.getlist('drop_cols')

        elif ',' in r.form[key]:
            inputs[key] = [str(i) for i in r.form[key].replace(',', '')]
            #inputs[key] = [str(0), str(1), str(2)]

        # all other but the list inputs
        else:
            inputs[key] = r.form[key]

    # convert types to python representations
    for key in inputs.keys():
        try:

            # first handle cases where the input is None
            if inputs[key] == 'None':
                inputs[key] = None

            # then handle any case where it is likely to be a number
            elif inputs[key].startswith(('0', '1', '2', '3', '4', '5',
                                         '6', '7', '8', '9')):

                # if it's a number with a decimal then convert to float
                if '.' in inputs[key]:
                    inputs[key] = float(inputs[key])

                # leave all other inputs as they are
                else:
                    inputs[key] = int(inputs[key])

        except AttributeError:
            pass

    return inputs
