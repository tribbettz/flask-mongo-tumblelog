from flask import Flask
from flask.ext.mongoengine import MongoEngine

def register_blueprints(app):
	from app.views import posts
	app.register_blueprint(posts)

app = Flask(__name__)
app.config["MONGODB_DB"] = 'my_tumble_log'
app.config["SECRET_KEY"] = '\xf0\xa8\x0ee\xc4+\x95}\x7fr\x1cRDAq4\xc8\xe6\x88\xde\x8e&Q\xe8'

db = MongoEngine(app)
register_blueprints(app)

if __name__ == '__main__':
	app.run()