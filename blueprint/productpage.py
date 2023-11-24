from flask import Flask,Blueprint,render_template

product_page=Blueprint(
    'product_page',__name__,static_folder='static',template_folder='templates'
)

@product_page.route('/')
def home():
    return render_template('index.html')