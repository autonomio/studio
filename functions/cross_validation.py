import numpy as np
from talos.utils.validation_split import kfold
from sklearn.metrics import f1_score
import tensorflow as tf

from functions.load_data import load_data

def cross_validation(inputs, model, folds=5):

	'''Performs cross_validation for n folds'''

	out = []

	x, y, _null_ = load_data(inputs) # data
	kx, ky = kfold(x, y, folds, True)

	for i in range(folds):
		model._make_predict_function()
		y_pred = model.predict(kx[i]) >= 0.5
		scores = f1_score(y_pred, ky[i], average='binary')
		out.append(scores * 100)

	return np.mean(out), np.sum(out), out