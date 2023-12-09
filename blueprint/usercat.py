from flask import Flask,redirect, url_for,request,flash,Blueprint, session as newsession
from model import Product,Cart
from connection import app, db
from sqlalchemy import and_
usercat=Blueprint(
    'usercat',__name__,
    static_folder='static',
    template_folder='templates'
)

@usercat.route('/addtocat/<int:id>',methods=['GET'])
def addtocat(id):
    user=newsession.get('userid')
    checkpro=Product.query.get_or_404(id)
    #checkcart=Cart.query.filter_by(productid=id).first()
   
    
    #  return redirect(request.referrer) if request.referrer else redirect('/default_page')
    if checkpro:
        checkcart = Cart.query.filter_by(userid=user, id=id).first()
        #checkcart = Cart.query.filter(and_(checkpro.id == id, Cart.userid == user)).first()

        
        if checkcart:
            
            checkcart.qty=checkcart.qty + 1
            checkcart.total=checkcart.total + checkpro.price
            #checkcart.userid=user
            try:
                db.session.commit()
                return redirect(request.referrer)
            except:
                return redirect(request.referrer)
        else:
            # no item in the cart
            print("pro oooooooooooooooooooooooo")
            newcart=Cart(
                productid=checkpro.id,
                total=checkpro.price,
                qty=1,
                userid=user
            )
            print("oooooooooooooooooooooooooooooo you")
            try:
                db.session.add(newcart)
                db.session.commit()
                return redirect(request.referrer)
            except:
                return redirect(request.referrer)
            
        return redirect(request.referrer)
        
    else:
        return redirect(request.referrer)
    