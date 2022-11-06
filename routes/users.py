from flask import Blueprint, render_template, url_for, abort, redirect, request, g, flash
from db import get_db

users = Blueprint('users', __name__)

@users.route("/login", methods=["GET"])
def login_get():
    flash("THIS IS A LOGIN PAGE!!! BE SAFE WITH YOUR CREDENTIALS")
    return render_template("users/login.html")

@users.route("/login", methods=["POST"])
def login_post():
    uname = request.form["uname"]
   
    password= request.form["password"]


    cur = get_db().cursor()

    cur.execute("SELECT fname, lname FROM `user` WHERE uname=%s AND password=%s", (uname, password))
    user = cur.fetchone()

    if user is None or password is None:
        return abort(400)

    return redirect(url_for("posts.create_new_post"))

@users.route("/users", methods=["GET"])
def users_list():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()

    return render_template("users/list.html", user=users)

@users.route("/user/<int:id>/delete", methods=["POST"])
def user_delete(id):
    cur.get_db().cursor()
    cur.execute("DELETE FROM user WHERE id=%s", (id,))
    get_db().commit()

    return render_template("users/register.html")

    