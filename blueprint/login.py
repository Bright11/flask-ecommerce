from flask import Flask,url_for,redirect,render_template,request,session,Blueprint,flash
from model import User
from connection import db, app
from forms import LoginForm
from flask_bcrypt import Bcrypt

loginuser=Blueprint(
    'loginuser',__name__,
    template_folder='templates',
    static_folder='static'
)
bcrypt=Bcrypt(app)

@loginuser.route('/login',methods=['GET','POST'])
def login():
    newuser=LoginForm()
    if newuser.validate_on_submit():
        print("user oooooooooooooooooo")
        user=User.query.filter_by(email=newuser.email.data.lower()).first()
        password=bcrypt.check_password_hash(user.password,newuser.password.data)
        if user:
           
            if password:
                session['username']=user.username
                session['email']=user.email 
                session['userid']=user.id
                return redirect(url_for('product_page.home'))
            else:
                flash("Password is not correct")
                return redirect(url_for('loginuser.login'))
        else:
            flash("User does not exist")
            return redirect(url_for('loginuser.login'))
    else:
        return render_template("pages/login.html",newuser=newuser)


