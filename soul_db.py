from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meet:123456@localhost/meet_db'
db = SQLAlchemy(app)

class Soul(db.Model):
    __tablename__ = "posts"
    id = db.Column('id', db.Integer, primary_key=True)
    nickname = db.Column('nickname', db.Unicode)
    quote = db.Column('quote', db.Integer)




db.create_all()
print('hi')