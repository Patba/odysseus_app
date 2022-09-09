from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = '1@FF4^fzxcs!!@4#dfsdfsdf'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///dbase.sqlite3'
app.permanent_session_lifetime = timedelta(minutes=15)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app.models.models import *
from app.main.routes import home
from app.user.routes import login
from app.requests.routes import new_request
from app.admin.routes import admin
from app.tickets.routes import tickets
from app.settings.routes import settings
from app.my_department.routes import my_departments
from app.future_functionalities.routes import future_functionalities


app.register_blueprint(home)
app.register_blueprint(login)
app.register_blueprint(new_request)
app.register_blueprint(admin)
app.register_blueprint(tickets)
app.register_blueprint(settings)
app.register_blueprint(my_departments)
app.register_blueprint(future_functionalities)


