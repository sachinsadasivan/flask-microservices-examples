from flask import Flask
from flask import render_template
from flask import request
import requests
import json


app = Flask(__name__)


# Declare App root
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/product-catalog', methods=['POST'])
def get_product_catalog():
    product_id = request.form['productId']
    r = requests.get('http://localhost:8081/product-catalog/' + str(product_id))
    return json.loads(r.text)


if __name__ == '__main__':
    app.run()