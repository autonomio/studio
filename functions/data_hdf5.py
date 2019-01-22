import pandas as pd


def store_hdf5(data, name):
    
    '''Creates a hdf5 based data storage.'''
    
    data_store = pd.HDFStore('/tmp/' + name + '.h5')
    
    data_store.put(name, data, encoding='UTF-8')

    data_store.close()

    
def retrieve_hdf5(name):
    
    '''Retrieves data from hdf5 based data storage'''
    
    # Access data store
    data_store = pd.HDFStore('/tmp/' + name + '.h5')

    # Retrieve data using key
    out = data_store[name]
    data_store.close()
    
    return out