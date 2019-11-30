from . import main
from flask import render_template
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
        password = reg_form.password.data
        
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()

    return render_template('signup.html', form=reg_form)