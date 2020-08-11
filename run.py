from flask import Flask
app = Flask(__name__)


posts = []


@app.route("/")
def index():
    return "{} posts".format(len(posts))


@app.route("/<string:slug>/")
def show_post(slug):
    return "Mostrando el post {}".format(slug)
