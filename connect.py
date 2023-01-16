from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from application import app

DEBUG = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Spirtovik@localhost:3306/words'

def connectDb():
    db = create_engine('mysql+pymysql://root:Spirtovik@localhost:3306/words')
    return db
