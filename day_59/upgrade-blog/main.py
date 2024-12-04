from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_endpoint = "https://api.npoint.io/a5992a4597cf09131377"
    response = requests.get(api_endpoint).json()
    return render_template("index.html", articles_data=response)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def post(index):
    api_endpoint = "https://api.npoint.io/a5992a4597cf09131377"
    response = requests.get(api_endpoint).json()
    for article in response:
        requested_post = None
        if article["id"] == index:
            requested_post = article
    return render_template("post.html",response=response, requested_post=requested_post)



if __name__ == '__main__':
    app.run(debug=True)