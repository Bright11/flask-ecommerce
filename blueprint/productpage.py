from flask import Flask,Blueprint,render_template
from model import Category,Product
from sqlalchemy.sql import func  # Import the func object
import random

product_page=Blueprint(
    'product_page',__name__,static_folder='static',template_folder='templates'
)

@product_page.route('/')
def home():
    #  random_items = Item.query.order_by(func.random()).limit(5).all()
    catandpost=Category.query.all()
    protopcat=Product.query.order_by(func.random()).limit(2).all()
    protopcat2=Product.query.order_by(func.random()).limit(2).all()
    bestdeal=Product.query.order_by(func.random()).limit(4).all()
    return render_template('pages/index.html',catandpost=catandpost,protopcat=protopcat,protopcat2=protopcat2,bestdeal=bestdeal)