from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for, make_response, request
import json
#literally importing the dictionary from options.py
from options import DEFAULTS


app = Flask(__name__)

def get_saved_data():
	try:
		data = json.loads(request.cookies.get('character'))
	except TypeError:
		data={}
	return data

@app.route('/')
def index():
	data = get_saved_data()
	return render_template('index.html', saves=data)

@app.route('/builder')
def builder():
	return render_template('builder.html', 
							saves=get_saved_data(), 
							options=DEFAULTS)

# methods lists the methods that is can accept, default is all the routes
@app.route('/save', methods=["POST"])
def save():
	#import pdb; pdb.set_trace()
	response = make_response(redirect(url_for('builder')))
	# update if there is saved data and send it back
	data = get_saved_data()
	data.update(dict(request.form.items()))
	response.set_cookie('character', json.dumps(data))
	return response


app.run(debug=True, host='0.0.0.0', port=8000)