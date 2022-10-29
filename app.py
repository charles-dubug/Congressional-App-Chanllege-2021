# from socket import fromshare
from socketserver import BaseRequestHandler
from tokenize import String
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
from flask_sslify import SSLify
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, StringField
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os


#mail config 
app = Flask('app')



app.secret_key = '12345678987654321'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hutimk@gmail.com'
app.config['MAIL_PASSWORD'] = 'qaimihqwugcdznfo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.secret_key = "123456789"

if 'DYNO' in os.environ: 
    sslify = SSLify(app)


#database 

cred = credentials.Certificate('./static/vertiblekey.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://vertible-d6c3f-default-rtdb.firebaseio.com'
})


def sendEmail(result):
    msg = Message("Contact Form from Website", sender="hutimk@gmail.com", recipients=["hutimk@gmail.com"])

    msg.body = """
    Hello there,

    You just received a contact form.

    Name: {}
    Email: {}
    Message: {}
    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)



@app.route("/", methods=['GET', 'POST'])
def home():
    return redirect(url_for("index"))


@app.route("/index.html", methods=['GET', 'POST'])
def index():
    if 'username' in session:
        return render_template("index.html", user = session['username'])
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        result = {}

        result['name'] = request.form['name']
        result['email'] = request.form['email'].replace(' ', '').lower()
        result['message'] = request.form['message']

        sendEmail(result)

        return render_template('contact.html', **locals())

    return render_template('contact.html', **locals())


@app.route("/videos.html")
def videos():
    return render_template('videos.html')

@app.route("/application.html")
def application():
    return render_template("application.html")

@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('account'))
    if request.method == 'POST':
        result = request.form
        if(result['password'] != result['cpassword']):
            return render_template("signup.html", data="The passwords were not the same!")
        else:
            ref = db.reference('/Users')
            arr = ref.get()
            arr = list(arr) 
            for i in range(len(arr)):
                if(ref.child(arr[i]).child('username').get() == result['username']):
                    return render_template("signup.html", data="The username is already taken!")
                elif(ref.child(arr[i]).child('email').get() == result['email']):
                    return render_template("signup.html", data="The email is already used! ")
            ref.push({ 
                        'email': result['email'],
                        'password': result['password'],
                        'username': result['username'],
                        'points': 0
                    })
            session['username'] = result['username']
            session['points'] = 0
            return redirect(url_for("index"))
    return render_template("signup.html", data="")

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form
        ref = db.reference('/Users')
        arr = ref.get()
        arr = list(arr)
        for i in range(len(arr)):
            if(ref.child(arr[i]).child('username').get() == result['username'] and ref.child(arr[i]).child('password').get() == result['password']):
                session['username'] = result['username']
                session['points'] = ref.child(arr[i]).child('points').get()
                return redirect(url_for("index"))
        return render_template("login.html", data="Your information could not be authorized!")

    return render_template("login.html")

@app.route("/account.html", methods=['GET', 'POST'])
def account():
    return render_template("account.html", user= session['username'], points=session['points'])

@app.route("/rewards.html")
def rewards():
    return render_template("rewards.html")

if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
