from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/test')
def test():
    return render_template('parallax-template/index.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')