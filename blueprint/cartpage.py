from flask import Flask,request,render_template,redirect,flash,Blueprint,session as newsession
from model import Cart
from connection import app,db
from sqlalchemy import func

cartpage=Blueprint(
    'cartpage',__name__,
    static_folder='static',
    template_folder='templates'
)

@cartpage.route('/cartpage',methods=['Get','POST'])
def viewvart():
    user=newsession.get('userid')
    cart=Cart.query.filter(Cart.userid==user).all()
    total_cart_price = Cart.query.filter(Cart.userid == user).with_entities(func.sum(Cart.total)).scalar() or 0
    return render_template('pages/cartpage.html',cart=cart,total_cart_price=total_cart_price)