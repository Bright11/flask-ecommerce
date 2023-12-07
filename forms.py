from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField,SubmitField,SearchField,BooleanField,FileField
from wtforms.validators import DataRequired,Length,Email,EqualTo


# USER FORM
class UserForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(), Email()])
    password=PasswordField("Password",[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(), EqualTo("password")])
    submit=SubmitField("Register")
    
    

class UserForm(FlaskForm):
    username=StringField("Username",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired(), Email()])
    password=PasswordField("Password",[DataRequired()])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(), EqualTo("password")])
    submit=SubmitField("Register")
    
    

class LoginForm(FlaskForm):
    email=StringField("Email",validators=[DataRequired(), Email()])
    password=PasswordField("Password",[DataRequired()])
    submit=SubmitField("Register")
    
class CategoryForm(FlaskForm):
    name=StringField('Category Name', validators=[DataRequired()])
    submit=SubmitField('Save')
    
    
# product
class ProductForm(FlaskForm):
    image=FileField("Image")
    submit=SubmitField('Save')


