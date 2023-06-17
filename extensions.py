from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_login import LoginManager

from flask_migrate import Migrate



db = SQLAlchemy(app)
migrate=Migrate(app,db)
login_manager=LoginManager(app)
