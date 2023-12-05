from flask import Flask, Blueprint,render_template,flash,redirect,url_for
from forms import CategoryForm,ProductForm
from model import Category,db, Product
import unicodedata
import re

admincategory=Blueprint(
    'admincategory',__name__, static_folder='static',template_folder='templates'
)

@admincategory.route('/addcategory',methods=['GET','POST'])
def addcategory():
    # adding category
    allcat=Category.query.all()
    pro=Product.query.all()
    catform=CategoryForm()
    proform=ProductForm()
    if catform.validate_on_submit():
        # forms validation
        checkcatexist=Category.query.filter_by(name=catform.name.data).first()
        if checkcatexist:
            flash(f'Category name already exist{catform.name.data}','error')
            return redirect(url_for('admincategory.addcategory'))
        else:
            slug=catform.name.data.lower()
            slug=slug.replace(' ','-')
            slug=unicodedata.normalize('NFKD',slug).encode('ascii','ignore').decode('utf-8')
            slug=re.sub(r'[-]+','-',slug)
            slug=slug.strip('-')
            category=Category(name=catform.name.data,slug=slug)
            
            db.session.add(category)
            db.session.commit()
            return redirect(url_for('admincategory.addcategory'))
    
    else:
        return render_template('admin/addcategory.html',allcat=allcat,catform=catform, proform=proform,pro=pro)