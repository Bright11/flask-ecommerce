from flask import Flask, render_template, url_for,flash,redirect
from blueprint.productpage import product_page


app=Flask(__name__)

app.register_blueprint(product_page)






if __name__=='__main__':
    app.run(debug=True)