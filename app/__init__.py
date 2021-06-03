from flask import Flask
from .routes import routes_register
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

routes_register(app)