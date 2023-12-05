from flask import Flask,render_template,flash, url_for,redirect,Blueprint,request
from model import Product,db
from connection import app

deletepro=Blueprint(
    'deletepro',__name__,
    static_folder='static',
    template_folder='templates'
)

@deletepro.route('/delete/<int:id>',methods=['GET'])
def deleteitem(id):
    datatodelete=Product.query.get(id)
    if datatodelete:
        db.session.delete(datatodelete)
        db.session.commit()
        flash("Product deleted")
        return redirect(request.referrer or url_for('admincategory.addcategory'))
    else:
        flash("No data found")
        return redirect(request.referrer or url_for('product_page.index'))



