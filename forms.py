from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField,SubmitField,SearchField,BooleanField,FileField
from wtforms.validators import DataRequired,Length,Email,EqualTo



class CategoryForm(FlaskForm):
    name=StringField('Category Name', validators=[DataRequired()])
    submit=SubmitField('Save')
    
    
# product
class ProductForm(FlaskForm):
    image=FileField("Image")
    submit=SubmitField('Save')


