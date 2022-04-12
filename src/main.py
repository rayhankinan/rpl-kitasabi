from application import app
from routes.akunRoutes import akunRoutes

def initialize_app():
    app.register_blueprint(akunRoutes, url_prefix="/akun")

if __name__ == "__main__":
    initialize_app()
    app.run(port=3000, debug=True)