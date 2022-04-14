from application import app
from routes.akunRoutes import akunRoutes
    
if __name__ == "__main__":
    app.register_blueprint(akunRoutes, url_prefix="/akun")

    app.run(port=3000, debug=True)