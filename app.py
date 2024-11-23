from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pathlib import Path
#importing backend logic
from static.authentication import process_data


path = Path("static/login.txt")

app = Flask(__name__)
CORS(app)

#This route is for the home page
@app.route('/')
def home():
    return render_template('index.html')

#Read my file backend
@app.route('/process-file', methods=['POST'])
def process_file():
    file_path = path
    if file_path.exists():
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({'content': content})
    else:
        return jsonify({'error': 'File not found'}), 404

#Get backend
@app.route('/process', methods=['POST'])
def process():
    data = request.json

    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    result = process_data(data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)