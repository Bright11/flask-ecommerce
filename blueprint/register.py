from flask import Flask,url_for,redirect,render_template,flash,request,Blueprint
from forms import UserForm
from connection import app,db
from model import User
from flask_bcrypt import Bcrypt

registration=Blueprint(
    'registration',__name__,
    static_folder='static',
    template_folder='templates'
)
bcrypt=Bcrypt(app)

@registration.route('/register',methods=['GET','POST'])
def register():
    newuser=UserForm()
    if newuser.validate_on_submit():
        print("yes ooooooooooooooooooooo")
        checkemail=User.query.filter_by(email=newuser.email.data).first()
        if checkemail:
            flash("This email already exist")
            return redirect(url_for('registration.register'))
        else:
            passwordhash=bcrypt.generate_password_hash(newuser.password.data).decode('utf-8')
            user=User(
                username=newuser.username.data,
                email=newuser.email.data.lower(),
                password=passwordhash,
            )
            db.session.add(user)
            db.session.commit()
            flash("Registration was successful")
            return redirect(url_for('loginuser.login'))
    else:
        return render_template('pages/register.html',newuser=newuser)