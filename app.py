from flask import Flask, render_template, url_for,flash,redirect
from blueprint.productpage import product_page 
from adminblueprint.addcategory import admincategory
from adminblueprint.addpro import addproduct
from adminblueprint.editpro import editpro
from adminblueprint.deletpro import deletepro
from model import db, Category
from connection import app


app.register_blueprint(product_page)
app.register_blueprint(admincategory)
app.register_blueprint(addproduct)
app.register_blueprint(editpro)
app.register_blueprint(deletepro)
# database configuration

db.init_app(app)

with app.app_context():
    db.create_all()

# getting categories for all pages
@app.context_processor
def globaldata():
    category=Category.query.all()
    
    return {'category':category}


if __name__=='__main__':
    app.run(debug=True)