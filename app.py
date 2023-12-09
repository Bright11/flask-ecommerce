from flask import Flask, render_template, url_for,flash,redirect,session as usersession
from blueprint.productpage import product_page 
from adminblueprint.addcategory import admincategory
from adminblueprint.addpro import addproduct
from adminblueprint.editpro import editpro
from adminblueprint.deletpro import deletepro
from blueprint.register import registration
from blueprint.usercat import usercat
from blueprint.login import loginuser
from blueprint.cartpage import cartpage
from blueprint.deletecart import deletecart
from blueprint.logout import logout
from model import  Category,Cart
from connection import app,db



app.register_blueprint(product_page)
app.register_blueprint(admincategory)
app.register_blueprint(addproduct)
app.register_blueprint(editpro)
app.register_blueprint(deletepro)
app.register_blueprint(registration)
app.register_blueprint(loginuser)
app.register_blueprint(usercat)
app.register_blueprint(cartpage)
app.register_blueprint(deletecart)
app.register_blueprint(logout)
# database configuration

db.init_app(app)

with app.app_context():
    db.create_all()

# getting categories for all pages
@app.context_processor
def globaldata():
    user=usersession.get('userid')
    category=Category.query.all()
    cart_count =Cart.query.filter_by(userid=user).count()
    
    return {'category':category,"cart_count":cart_count}


if __name__=='__main__':
    app.run(debug=True)