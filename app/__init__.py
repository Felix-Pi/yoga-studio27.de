from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_breadcrumbs import Breadcrumbs
from app.config import Config

app = Flask(__name__, template_folder='../templates/', static_folder='../static/')

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# from app.models.User import *


from app.routes.home import bp as home_bp
from app.routes.tpl import bp as tpl_bp


app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(tpl_bp, url_prefix='/tpl')


from app import routes

app.logger.setLevel(Config.log_level)
