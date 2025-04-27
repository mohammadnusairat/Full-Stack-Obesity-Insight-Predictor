from flask_pymongo import PyMongo

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)

def get_user_collection():
    return mongo.db.users
