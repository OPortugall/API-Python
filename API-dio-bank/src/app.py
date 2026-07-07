import os

from flask import Flask, json
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from src.models import db
from werkzeug.exceptions import HTTPException

migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()

def create_app(enviroment = os.environ["ENVIRONMENT"]):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f"src.config.{enviroment.title()}Config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)

    from src.controllers import auth, post, role, user

    app.register_blueprint(post.app)
    app.register_blueprint(user.app)
    app.register_blueprint(auth.app)
    app.register_blueprint(role.app)

     

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
            "code": e.code,
            "name": e.name,
            "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response

    return app