from main import main
from app import App
from src.config import config

if __name__ == '__main__':
    static_folder = os.path.join(os.path.dirname(__file__), '../front/build')
    app = App(port=5001, static=static_folder)
    app.add_db(db_url=config.MONGO_URL)
    app.create_router()
    app.create_server()