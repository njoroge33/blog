from . import main
from werkzeug.security import generate_password_hash
from flask import render_template,flash, redirect, url_for
from flask_login import login_user, current_user
from .forms import *
from ..models import *
from .. import db

@main.route('/',methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()

    if reg_form.validate_on_submit():
        email = reg_form.email.data
        username = reg_form.username.data
        password = generate_password_hash(reg_form.password.data)
        
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('signup.html', form=reg_form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    #login if validation is successful
    if login_form.validate_on_submit():
        user_object =User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('main.profile',uname=login_form.username.data))
        

    return render_template('login.html', form=login_form)

@main.route('/user/<uname>', methods=['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))

    return render_template("profile.html", user=user)