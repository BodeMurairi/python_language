from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
    else:
        error = 'Please enter your name/password.'
    return f'<h1> Name: {name} Password: {password} </h1>'




if __name__ == '__main__':
    app.run(debug=True)