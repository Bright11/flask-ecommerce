from flask import Flask,render_template,request,Blueprint,flash,redirect,url_for
from forms import ProductForm
from model import Product,db
import unicodedata
import re
from werkzeug.utils import secure_filename
from connection import app
import uuid as uuid
import os


addproduct=Blueprint(
    'addproduct',__name__,
    static_folder='static',
    template_folder='templates'
)

UPLOAD_FOLDER='static/productimg'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS']={ 'png', 'jpg', 'jpeg', 'webp','jfif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@addproduct.route('/addproduct',methods=['POST'])
def addpro():
    proform=ProductForm()
    if request.method=='POST':
       # print("hhhhhhhhhhhhhhhhhhhhhhhhhhh")
        # slug
        slug=request.form.get('name').lower()
        #print(slug)
        slug=slug.replace(' ','-')
        slug=unicodedata.normalize('NFKD',slug).encode('ascii','ignore').decode('utf-8')
        slug=re.sub(r'[-]+', '-',slug)
        slug=slug.strip('-')
        # upload file
        #print("mycateid",request.form.get('catid'))
        #print(request.files['image'] )
        uploadfile=proform.image.data
        if uploadfile and allowed_file(uploadfile.filename):
            print("great let's go")
            uniquename=str(uuid.uuid4())+ secure_filename(uploadfile.filename)
            filepath=os.path.join(app.config['UPLOAD_FOLDER'],uniquename)
            uploadfile.save(filepath)
            newproduct=Product(
                name=request.form.get('name'),
                description=request.form.get('description'),
                image=uniquename,
                discount=int(request.form.get('discount')),
                price=float(request.form.get('price')),
                slug=slug,
                catid=int(request.form.get('catid'))
            )
            db.session.add(newproduct)
            db.session.commit()
            flash("product created")
            return redirect(url_for('admincategory.addcategory'))
    else:
         return redirect(url_for('admincategory.addcategory'))
    return redirect(url_for('admincategory.addcategory'))



