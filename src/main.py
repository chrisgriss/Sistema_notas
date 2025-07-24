from flask import Flask, session
from flask_cors import CORS
#from src.Blueprints_base.urls import urls_bp
from Blueprints_base.urls import urls_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = ('carro')

    app.register_blueprint(urls_bp, url_prefix='/api/')
    CORS(app, supports_credentials=True, resources={r'/api/*': {'origins': '*'}})
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)