
from main import app

@app.route('/index')
def indexcontroller():
    return "Server index page"
