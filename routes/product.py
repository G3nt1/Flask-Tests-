from flask import Blueprint, render_template, g, request, redirect, url_for, abort
from db import get_db

prod = Blueprint('prod', __name__)

@prod.route("/products/new", methods=["GET"])
def products_new_form():
    return render_template("products/new.html")

@prod.route("/products/new", methods=["POST"])
def products_new():
    prod = request.form['prod']
    price = request.form['price']
    desc = request.form["desc"]

    cur = get_db().cursor()
    cur.execute("INSERT INTO products (product, price, `desc`) VALUES(%s, %s, %s)", (prod, price,desc))
    get_db().commit()
    
    return redirect(url_for("prod.products_list"))


@prod.route("/products", methods=["GET"])
def products_list():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM products")
    prod = cur.fetchall()

    return render_template("products/list.html", products=prod)