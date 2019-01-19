from flask import Flask 

app = Flask(__name__) # Gives a file a unique name

@app.route('/')
def home():
	return "Hello, world!"

app.run(port=5000, debug=True)
