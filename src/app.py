from flask import Flask
from users import handlers
from common import static_handler
from flask_cors import CORS
from ofp import ofp_handlers


class App:
    app: Flask
    port: int
    host: str
    debug: bool
    static_folder: str

    def __init__(self, port: int, static: str, debug=True):
        self.port = port
        self.debug = debug
        self.static_folder = static
        self.app = Flask(__name__, static_folder=self.static_folder, static_url_path="")
        CORS(self.app)

    def create_server(self):
        self.app.run(host="localhost", port=self.port, debug=self.debug)

    def create_router(self):
        self.app.register_blueprint(static_handler.bp)
        self.app.register_blueprint(handlers.users)
        self.app.register_blueprint(ofp_handlers.ofp)
