from flask import Flask
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/', serverSelectionTimeoutMS=2000)
app = Flask(__name__)


@app.route('/')
def hello():
    print("hello world")
    return "hello world" 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)