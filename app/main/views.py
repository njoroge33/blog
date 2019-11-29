from . import main
from flask import render_template
from .forms import *

@main.route('/',methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@main.route('/signup' , methods=['GET', 'POST'])
def signup():

    reg_form = RegistrationForm()
    return render_template('signup.html', form=reg_form)