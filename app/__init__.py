


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from flask_wtf.csrf import CsrfProtect


csrf = CsrfProtect()


csrf.init_app(app)

from app import views, models
