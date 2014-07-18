import os
from flask import Flask, render_template
import income

app = Flask(__name__)

@app.context_processor
def screeners():
	return {'income_stocks':income.stocks}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/income')
def income_screener():
	return render_template('income.html')

if __name__ == '__main__':
	app.run(debug=True)