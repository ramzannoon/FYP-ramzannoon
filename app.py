from flask import Flask, render_template, request, url_for, redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
import os
import random
db_path=os.path.join(os.path.dirname(__file__))
db_uri='sqlite:///'+os.path.join(db_path, 'mydb.sqlite')

app=Flask(__name__)
app.config['SECRET_KEY']='thisissecrethere'
app.config['SQLALCHEMY_DATABASE_URI']=db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app)
admin= Admin(app)

class Role(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(60))
    password=db.Column(db.String(70))

admin.add_view(ModelView(Role, db.session))


@app.route('/')
def index():
    csc='dbmvnvbmnvvxcv'
    password=''
    for i in range(5):
        password+= random.choice(csc)

    return render_template('index.html')

@app.route('/admindashboard')
def admindashboard():
    return render_template('admindashboard.html')

@app.route('/template', methods=['GET', 'POST'])
def template():
    return render_template('template.html')

@app.route('/templateteacher', methods=['GET', 'POST'])
def templateteacher():
    return render_template('templateteacher.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method=='POST':
        name=request.form.get('here')
        if name=='Student':
            return redirect(url_for('template'))
        else:
            return redirect(url_for('templateteacher'))
    return render_template('login.html')


if __name__=='__main__':
    app.run(debug=True)