from flask_restplus import Resource
from main import app
from main import api

@api.route('/index')
class IndexController(Resource):
    def get(self):
        return "Server index page"
