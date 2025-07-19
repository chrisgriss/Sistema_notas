from flask import Flask
from flask_cors import CORS
from home_project_.urls import urls_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'FNDOISGAY'
    app.register_blueprint(urls_bp, url_prefix='/api')
    CORS(app, supports_credentials=True)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug = True, port=5000)