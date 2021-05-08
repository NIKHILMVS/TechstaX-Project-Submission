from flask_pymongo import PyMongo
from flask import Flask
app=Flask(__name__)

# Setup MongoDB here
client = PyMongo(app,uri="mongodb://localhost:27017/database")
