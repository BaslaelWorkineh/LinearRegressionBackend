from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)

    from .data_visualization import data_visualization_bp
    from .prediction import prediction_bp

    app.register_blueprint(data_visualization_bp)
    app.register_blueprint(prediction_bp)

    return app
