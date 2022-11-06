from flask import Blueprint, render_template, redirect, url_for, request, abort, flash
from db import get_db

auth = Blueprint('auth', __name__)

@auth.route("/register", methods=["GET"])
def home_get():
    flash("This is a Register Page..You can Register here With your credentials")
    
    return render_template("users/register.html")


@auth.route("/register", methods=['POST'])
def home_post():

    fname = request.form['fname']
    lname = request.form['lname']
    uname = request.form['uname']
    pas = request.form['pass']
    
    cur = get_db().cursor()
    cur.execute("INSERT INTO `user`(fname,lname,uname,password) VALUES(%s, %s,%s,%s)", (fname,lname,uname,pas)) 
    get_db().commit()
  
        
    return redirect(url_for("users.login_post"))

