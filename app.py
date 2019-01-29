from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    title = "Flask Web App"
    paras = [
        'section 1',
        'section 2',
        'stction 3'
    ]    
    return render_template("index.html", title=title,data=paras)

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)