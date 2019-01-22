import talos as ta
from functions.simple_neural_net import simple_neural_net
from functions.params import default_params


def run_optimize(x, y, mode='auto', params=None, grid_downsample=1):

	if mode == 'auto':
		scan_object = ta.Scan(x, y,
							  model=simple_neural_net,
							  params=default_params(),
							  grid_downsample=grid_downsample)
	else:
		scan_object = ta.Scan(x, y, model=simple_neural_net, params=params)

	return scan_object.data
