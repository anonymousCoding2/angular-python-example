from flask import Flask, jsonify

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/data', methods=['GET'])
def get_data():
	data = {
		'title': 'Welcome to Angular-Python App',
		'message': 'This is an example integration between Angular and Python!'
	}
	response = jsonify(data)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	