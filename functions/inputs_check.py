import ast


def inputs_check(inputs):

    '''Handles the case where the inputs is not coming
    from the user input in config view'''

    # for the case where the inputs are first time ingested
    try:
        inputs['data']
        with open('/tmp/' + 'inputs.studio.txt', 'w') as f:
            f.write(str(inputs))
            f.close()

    # for the case where the inputs are already ingested
    except KeyError:
        with open('/tmp/' + 'inputs.studio.txt', 'r') as f:
            s = f.read()
            f.close()
            # convert the string to dictionary
            inputs = ast.literal_eval(s)

    return inputs
