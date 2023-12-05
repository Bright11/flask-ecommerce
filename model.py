from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

# category model
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True)
    slug=db.Column(db.String(100),unique=True)
    # relationship
    product=db.relationship('Product',backref='category',lazy=True)
    def __repr__(self):
        return f'Category(`{self.name}`)'
    
    
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    catid=db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    name=db.Column(db.String(200),nullable=False)
    slug=db.Column(db.String(200),nullable=False,unique=True)
    price=db.Column(db.Float, nullable=False)
    discount=db.Column(db.Integer,default=0)
    image=db.Column(db.String(250),nullable=False)
    description=db.Column(db.Text,nullable=False)
    posteddate=db.Column(db.DateTime,default=datetime.utcnow)
    viewed=db.Column(db.Integer,default=0)
    def __repr__(self):
        return f"Product('{self.name}','{self.posteddate}')"










