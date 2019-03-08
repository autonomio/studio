import talos as ta
from functions.simple_neural_net import simple_neural_net
from functions.params import default_params


def run_optimize(x, y, mode='auto', params=None, grid_downsample=1, epochs=10):

    if mode == 'auto':
        params = default_params()
        params['epochs'] = [epochs]
        scan_object = ta.Scan(x, y,
                              model=simple_neural_net,
                              params=params,
                              grid_downsample=grid_downsample)
    else:
        scan_object = ta.Scan(x, y, model=simple_neural_net, params=params)

    cols = ['val_acc', 'val_loss', 'acc', 'loss']
    scan_object.data[cols] = scan_object.data[cols].astype(float).round(3)

    return scan_object.data
