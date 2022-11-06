from flask import Flask, render_template, g, abort, flash, request, redirect

import db

from routes.authentication import auth
from routes.post import post
from routes.product import prod
from routes.users import users
from routes.books import books

app = Flask(__name__)
app.config['SECRET_KEY'] = "G3NT!"

app.register_blueprint(auth)
app.register_blueprint(post)
app.register_blueprint(prod)
app.register_blueprint(users)
app.register_blueprint(books)


@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/search", methods=["GET"])
def search ():
        search = request.args['books']
        search = '%' + search + '%'


        cur = db.get_db().cursor()
        cur.execute("SELECT * FROM books WHERE title LIKE %s or author like %s or desctription LIKE %s", (search, search, search,))
        results = cur.fetchall()

        return render_template("books/list.html",books=results)

    

    
if __name__ == "__main__":
    app.run(debug=True)
