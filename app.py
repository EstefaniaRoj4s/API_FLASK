from flask import Flask, render_template, request, redirect, url_for
from models import Blog, Post

# Inicializar Flask
app = Flask(__name__)

# Crear instancia del Blog
blog = Blog("Mi Mini Blog")

# Rutas principales
@app.route("/")
def index():
    return render_template("index.html", posts=blog.posts)

@app.route("/add", methods=["GET", "POST"])
def add_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        post = Post(title, content)
        blog.add_post(post)
        return redirect(url_for("index"))
    return render_template("add_post.html")

@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    blog.delete_post(post_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
