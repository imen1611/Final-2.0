from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import initialize_routes
from configPack import mongo , mail
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

mongo.init_app(app)
mail.init_app(app)
api = Api(app)
initialize_routes(api)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
if __name__ == '__main__':
    app.run()