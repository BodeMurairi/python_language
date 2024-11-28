import requests
from flask import Flask, render_template
from post import Post

my_post = Post()

app = Flask(__name__)

@app.route('/')
def home():
    title_1 = my_post.posts[0]["title"]
    subtitle_1 = my_post.posts[0]["subtitle"]
    title_2 = my_post.posts[1]["title"]
    subtitle_2 = my_post.posts[1]["subtitle"]
    title_3 = my_post.posts[2]["title"]
    subtitle_3 = my_post.posts[2]["subtitle"]

    return render_template("index.html", first_title = title_1, first_subtitle= subtitle_1, second_title= title_2, second_subtitle = subtitle_2, third_title= title_3, third_subtitle = subtitle_3)

@app.route('/blog/article/<int:id>')
def first_article(id):
    article_title = my_post.posts[0]["title"]
    body = my_post.posts[0]["body"]
    return render_template("post.html", article_title = article_title, body = body)

@app.route('/blog/article/<int:id>')
def second_article(id):
    article_title = my_post.posts[1]["title"]
    body = my_post.posts[1]["body"]
    return render_template("post.html", article_title = article_title, body = body)


@app.route('/blog/article/<int:id>')
def third_article(id):
    article_title = my_post.posts[2]["title"]
    body = my_post.posts[2]["body"]
    return render_template("post.html", article_title = article_title, body = body)


if __name__ == "__main__":
    app.run(debug=True)
