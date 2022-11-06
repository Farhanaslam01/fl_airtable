from flask import Flask
from views import views


app = Flask(__name__)
app.register_blueprint(views,url_prefix="/") #after slash add page name


if __name__ == '__main__':
    app.run(debug=False, port=8000, host="0.0.0.0")