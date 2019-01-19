from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
	{
		'name': 'my wonderful store',
		'items': [
			{
				'name': 'my item',
				'price': 15.99			  
			}
		]
	}
]

# POST - used to receive data
# GET - used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
	pass 

# GET /store 
@app.route('/store')
def get_stores():
	return jsonify({'stores': stores}) #you can't return a list

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>', methods=['POST'])
def create_item_in_store(name):
	pass

# GET /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
	pass 


app.run(port=5000, debug=True)