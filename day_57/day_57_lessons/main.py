from flask import Flask, render_template
import random
from datetime import datetime
import requests




app = Flask(__name__)

@app.route('/')
def index():
    random_number = random.randint(1, 100)
    years = datetime.today().year
    return render_template("index.html", num = random_number, years = years)


@app.route('/guess/<string:name>')
def guess(name):
    agify_url_endpoint = f"https://api.agify.io?name={name}"
    genderize_url_endpoint = f"https://api.genderize.io?name={name}"
    age_data = requests.get(agify_url_endpoint, params= params).json()
    age = age_data['age']
    genderize_data = requests.get(genderize_url_endpoint, params= params).json()
    gender = genderize_data['gender']
    probability = genderize_data['probability']
    return render_template("guess.html", name = name,
                           age = age, gender = gender, probability = probability)



@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = " https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)

if __name__ == '__main__':
    app.run(debug=True)