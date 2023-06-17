from flask import Flask
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@127.0.0.1:3306/project1"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "projectt"

from controllers import *
from extensions import *
from models import *

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Reflect and create database tables
with app.app_context():
    db.reflect()
    db.create_all()



if __name__ == "__main__":
    app.run(port=5000, debug=True)

admin = Admin(app, name='myadmin')

admin.add_view(ModelView(Product,db.session))
admin.add_view(ModelView(category,db.session))