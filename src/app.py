from flask import Flask
from users import users_handlers
from atran import atran_handlers
from common import static_handler
from flask_cors import CORS
from ofp import ofp_handlers
from mongoengine import connect
from pymongo import errors
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response


class App:
    app: Flask
    port: int
    host: str
    debug: bool
    static_folder: str
    db_url: str

    def __init__(self, port: int, static: str, debug=True):
        self.port = port
        self.debug = debug
        self.static_folder = static
        self.app = Flask(__name__, static_folder=self.static_folder, static_url_path="")
        CORS(self.app)

    def add_db(self, db_url):
        self.db_url = db_url
        try:
            connect(host=db_url)
            print('DB connected')
        except errors.ConnectionFailure:
            print(errors.ConnectionFailure)

    def create_server(self):
        self.app.wsgi_app = DispatcherMiddleware(Response('Not found', status=404), {'/api/v1': self.app.wsgi_app})
        self.app.run(host="localhost", port=self.port, debug=self.debug)

    def create_router(self):
        routes = [
            {
                'name': "static",
                'handler': static_handler.bp
            },
            {
                'name': "users",
                'handler': users_handlers.users
            },
            {
                'name': "ofp",
                'handler': ofp_handlers.ofp
            },
            {
                'name': "atran",
                'handler': atran_handlers.atran
            }
        ]

        for route in routes:
            self.app.register_blueprint(route['handler'])
