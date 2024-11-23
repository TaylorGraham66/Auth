from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/example-endpoint', methods=['GET', 'POST'])
def example_function():
    # Call your backend logic here
    return jsonify({'message': 'Hello, Flask!'})



if __name__ == '__main__':
    app.run(debug=True)