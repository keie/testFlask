from flask import Flask, request, Response, jsonify, json, send_from_directory, abort
import os
from keras.models import load_model
app = Flask(__name__)


@app.route('/')
def index():
	return 'Hello IIS from Flask framework. :D 2'

@app.route('/Hello')
def hello_world():
	return 'Hello World!'
	
if __name__ == '__main__':
	app.run()
