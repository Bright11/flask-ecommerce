from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

app=Flask(__name__)

app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///productdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
