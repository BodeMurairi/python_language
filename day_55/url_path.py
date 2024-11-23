from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1 style = "text-align: center">Hello World</h1> '
            '<p style="color:blue"><a href="/home">Home</a></p>'
            '<img src=https://giphy.com/embed/YRVP7mapl24G6RNkwJ" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/moodman-YRVP7mapl24G6RNkwJ">via GIPHY>')

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"
@app.route('/<name>')
def greet(name):
    return f"Hello there, {name}"
if __name__ == '__main__':
    app.run(debug=True)