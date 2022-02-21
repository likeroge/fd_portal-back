from flask import Flask, send_from_directory, render_template
from src.users import users_handlers
from src.atran import atran_handlers
from src.aircraft import aircraft_handlers
from flask_cors import CORS
from src.ofp import ofp_handlers
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
    frontend_app: Flask

    def __init__(self, port: int, static: str, debug=True):
        self.port = port
        self.debug = debug
        self.static_folder = static
        # self.app = Flask(__name__, static_folder=self.static_folder, static_url_path="")
        self.app = Flask(__name__)
        self.frontend_app = Flask(__name__, static_folder='../front/build', static_url_path='')

        @self.frontend_app.errorhandler(404)
        def test_route(e):
            print(e)
            # return send_from_directory('../front/build', 'index.html')
            return send_from_directory(self.frontend_app.static_folder, 'index.html')
        CORS(self.app)

    def add_db(self, db_url):
        self.db_url = db_url
        try:
            connect(host=db_url)
            print('DB connected')
        except errors.ConnectionFailure:
            print(errors.ConnectionFailure)

    def create_server(self):
        self.app.wsgi_app = DispatcherMiddleware(Response('Not found', status=404), {'/api/v1': self.app.wsgi_app,
                                                                                     '': self.frontend_app})

        # self.app.wsgi_app = DispatcherMiddleware(self.frontend_app)
        # self.app.wsgi_app = DispatcherMiddleware(self.frontend_app, {'/api/v1': self.app})

        # self.app.run(host="localhost", port=self.port, debug=self.debug)
        self.app.run()

    def create_router(self):
        routes = [
            # {
            #     'name': "static",
            #     'handler': static_handler.bp
            # },
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
            },
            {
                'name': "aircraft",
                'handler': aircraft_handlers.aircraft
            },
        ]

        for route in routes:
            self.app.register_blueprint(route['handler'])
