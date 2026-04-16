from flask import Flask, render_template, request

import requests
BACKEND_URL = 'http://0.0.0.0:9000'
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    todo_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit',json=todo_data)
    return "todo_data submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)