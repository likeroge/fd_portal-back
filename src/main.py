import os
from app import App


def main():
    static_folder = os.path.join(os.path.dirname(__file__), '../../front/build')
    app = App(port=5001, static=static_folder)
    app.add_db(db_url='mongodb://193.187.175.206:27017/FDops')
    app.create_router()
    app.create_server()


if __name__ == '__main__':
    main()


