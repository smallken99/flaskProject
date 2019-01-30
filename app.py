from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    title = "Flask Web App"
    paras = [
        'section 1',
        'section 2',
        'stction 3'
    ]    
    return render_template("index.html", title=title,data=paras)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        pass
    return render_template("register.html",form=form)

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)