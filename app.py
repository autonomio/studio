from flask import Flask, render_template, request

from views.training_view import training_view
from views.predict_result_view import predict_result_view
from views.dataframe_view import dataframe_view
from views.optimize_process_view import optimize_process_view
from views.wrangle_view import wrangle_view
from views.wrangle_process_view import wrangle_process_view
from views.wrangle_save_view import wrangle_save_view


app = Flask(__name__, static_url_path='')

@app.route("/", methods=['GET'])
def studio(): 
	return render_template('studio.html')

@app.route("/training", methods=['GET', 'POST'])
def training():
	return training_view(request) 

@app.route("/wrangle", methods=['GET'])
def wrangle():
	return wrangle_view()

@app.route("/wrangle_process", methods=['GET', 'POST'])
def wrangle_process():
	return wrangle_process_view(request)

@app.route('/wrangle_save', methods=['GET','POST'])
def wrangle_save():
	return wrangle_save_view()

@app.route('/optimize', methods=['GET'])
def optimize():
	return render_template('optimize.html')

@app.route('/optimize_result', methods=['GET', 'POST'])
def optimize_result():
	return optimize_process_view(request)

@app.route("/predict", methods=['GET'])
def predict():
	return render_template('predict.html')

@app.route('/predict_result', methods=['GET', 'POST'])
def predict_result():
	return predict_result_view(request)

@app.route("/dataframe", methods=["GET"])
def dataframe():
	return dataframe_view()

if __name__ == "__main__":
	app.config.update(TEMPLATES_AUTO_RELOAD = True)
	app.run(debug=True)
