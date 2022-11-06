from flask import Blueprint, render_template, g, request, redirect, url_for, abort
from db import get_db
post = Blueprint('posts',__name__)


@post.route("/posts/new", methods=["GET"])
def create_new_post_form():
    return render_template("posts/new.html")


@post.route("/posts/new", methods=["POST"])
def create_new_post():
    title = request.form["title"]
    body = request.form["body_post"]

    if title is None or body is None:
        return abort(400)

    cur = get_db().cursor()
    cur.execute("INSERT INTO post (title, body) VALUE(%s, %s)", [title, body])
    get_db().commit()

    return redirect(url_for("posts.create_new_post", post_id=cur.lastrowid))


@post.route("/posts",  methods=["GET"])
def posts_list():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM post")
    post = cur.fetchall()

    return render_template("posts/list.html", posts=post)  

@post.route("/posts/<int:id>")
def post_show(id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM post WHERE id=%s", [id])
    post = cur.fetchone()

    if post is None:
        return abort(404)

    return render_template("posts/show.html", post=post)

@post.route("/posts/<int:id>/delete", methods=['POST'])
def post_delete(id):
    cur = get_db().cursor()
    cur.execute("DELETE FROM post WHERE ID=%s", (id,))
    get_db().commit()

    return redirect(url_for("posts.posts_list"))


    