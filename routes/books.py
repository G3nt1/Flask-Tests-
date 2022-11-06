from flask import Blueprint, redirect, render_template, url_for, g, abort, request
from db import get_db

books = Blueprint("books", __name__)

@books.route("/books/new", methods=["GET"])
def new_book():

    return render_template("books/new.html")

@books.route("/books/new", methods=["POST"])
def add_new_book():
    title = request.form["title"]
    auth = request.form["author"]
    desc = request.form["desctription"]

    if title is None or auth is None or desc is None:
        return abort(400)

    cur = get_db().cursor()
    cur.execute("INSERT INTO books (title, author,desctription) VALUES(%s, %s, %s)",(title,auth,desc,))
    get_db().commit()

    return render_template("books/new.html")

@books.route("/books", methods=["GET"])
def books_list():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM books")
    books = cur.fetchall()
    return render_template("books/list.html", books=books)

@books.route("/books/<int:id>/delete", methods=["POST"])
def delete_books(id):
    cur = get_db().cursor()
    cur.execute("DELETE FROM books WHERE id=%s", (id,))
    get_db().commit()

    return redirect(url_for("books.books_list"))
