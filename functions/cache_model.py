from keras.models import model_from_json


def save_model_as(model, path):

    '''Model Saver
    WHAT: Saves a trained model so it can be loaded later
    for predictions by predictor().
    '''

    model_json = model.to_json()
    with open('/tmp/' + path + ".json", "w") as json_file:
        json_file.write(model_json)
    json_file.close()

    model.save_weights(path + ".h5")


def activate_model(path):

    json_file = open('/tmp/' + path + ".json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    model = model_from_json(loaded_model_json)
    model.load_weights(path + '.h5')

    return model