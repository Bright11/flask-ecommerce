from flask import Flask, render_template,flash,redirect,request,url_for,Blueprint

from forms import ProductForm
from werkzeug.utils import secure_filename
from model import Product,db,Category
import os 
import uuid as uuid
import re 
import unicodedata
from connection import app

editpro=Blueprint(
    'editpro',__name__,
    static_folder='static',
    template_folder='templates'
)

UPLOAD_FOLDER='static/productimg'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']={ 'png', 'jpg', 'jpeg', 'webp','jfif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
        

@editpro.route('/editpro/<int:id>',methods=['GET','POST'])
def edititem(id):
  
    pro=Product.query.get_or_404(id) 
    allcat=Category.query.all()
    proform=ProductForm()
    if proform.validate_on_submit():
       
         # working with slug
        slug=request.form.get('name').lower()
        slug=slug.replace(' ','-')
        slug=unicodedata.normalize('NFKD',slug).encode('ascii','ignore').decode('utf-8')
        slug=re.sub(r'[-]+','-',slug)
        slug=slug.strip('-')
        # # working with image
        uploadfile=proform.image.data
        if uploadfile and allowed_file(uploadfile.filename):
            
            uniquename=str(uuid.uuid4())+ secure_filename(uploadfile.filename)
            filepath=os.path.join(app.config['UPLOAD_FOLDER'],uniquename)
            uploadfile.save(filepath)
            pro.catid=int(request.form.get('catid'))
            pro.name=request.form.get('name')
            pro.slug=slug
            pro.price=float(request.form.get('price'))
            pro.discount=int(request.form.get('discount'))
            pro.image=uniquename
            pro.description=request.form.get('description')
            print("here is the form",request.form)
           
            try:
                db.session.commit()
                return redirect(url_for('admincategory.addcategory'))
                
            except Exception as e:
                print(f"Error committing to the database: {e}")
                db.session.rollback()
                flash("there was an error")
                return redirect(url_for('editpro.edititem',id=id))
            
        else:
            pro.catid=int(request.form.get('catid'))
            pro.name=request.form.get('name')
            pro.slug=slug
            pro.price=float(request.form.get('price'))
            pro.discount=int(request.form.get('discount'))
           # pro.image=uniquename
            pro.description=request.form.get('description')
            print("here is the form",request.form)
           
            try:
                db.session.commit()
                return redirect(url_for('admincategory.addcategory'))
                
            except Exception as e:
                print(f"Error committing to the database: {e}")
                db.session.rollback()
                flash("there was an error")
                return redirect(url_for('editpro.edititem',id=id))
            
    else:
        return render_template('admin/editproduct.html',proform=proform,pro=pro,allcat=allcat)