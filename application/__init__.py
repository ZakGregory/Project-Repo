from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=
app.config['SECRET_KEY'] =

db = SQLAlchemy(app)

from application import models, routes
