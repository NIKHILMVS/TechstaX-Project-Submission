from flask import Flask

from app.webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    app.secret_key = 'super secret key'
    
    return app
