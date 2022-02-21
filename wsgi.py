# from main import main
# from app import App
from app import App
from src.config import config
from flask import Flask
import os

# if __name__ == '__main__':
    # static_folder = os.path.join(os.path.dirname(__file__), '../front/build')
    # app = App(port=5001, static=static_folder)
    # app.add_db(db_url=config.MONGO_URL)
    # app.create_router()
    # app.create_server()

static_folder = os.path.join(os.path.dirname(__file__), '../front/build')
app = App()
app.add_db(db_url=config.MONGO_URL)
app.create_router()
app.create_server()

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return 'Hello, World!'

