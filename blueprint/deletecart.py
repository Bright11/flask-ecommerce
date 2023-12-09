from flask import Flask,redirect,session as userseesion,url_for,flash,Blueprint,request
from connection import db, app
from model import Cart

deletecart=Blueprint(
    'deletecart',__name__,
)

@deletecart.route('/deleteusercart/<int:id>',methods=['GET'])
def deleteusercart(id):
    # datatodelete = Product.query.filter((Product.id == id) & (Product.userid == userid)).first()
    user=userseesion.get('userid')
    checkcart=Cart.query.filter((Cart.id==id) & (Cart.userid==user)).first()
    if checkcart:
        db.session.delete(checkcart)
        db.session.commit()
        return redirect(request.referrer )
    else:
        return redirect(request.referrer )
    