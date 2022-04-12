from routes.routes import routed_app

if __name__ == "__main__":
    routed_app.run(port=3000, debug=True)