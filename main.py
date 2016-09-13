from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app)

from controllers import *

if __name__ == "__main__":
    app.run()

