import os
from app import App


static_folder = os.path.join(os.path.dirname(__file__), '../../front/build')

if __name__ == '__main__':
    app = App(port=5001, static=static_folder)
    app.create_router()
    app.create_server()


