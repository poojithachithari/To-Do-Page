
import os
from dotenv import load_dotenv
from flask import Flask, request
import pymongo
load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')
client = pymongo.MongoClient(MONGO_URL)
db = client.test
collection = db['To-do-list']
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    todo_data = dict(request.json)
    collection.insert_one(todo_data)
    return "To-do item added successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)