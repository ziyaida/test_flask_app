from flask import Flask, render_template, request, redirect
from peewee import * 
from models import Post

app = Flask(__name__)

@app.route('/') 
def mike():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)

@app.route('/create/', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        password = request.form['password']

        Post.create(
            name = name,
            surname = surname,
            password = password
        )
        return redirect('/')
    return render_template('create.html')


if __name__ == "__main__":
    app.run(debug=True)