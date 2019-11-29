from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError, Email

class RegistrationForm(FlaskForm):
    """Restration form"""
    email = StringField('Email:',validators=[InputRequired(),Email()])
    username = StringField('Username:', validators=[InputRequired(message='Username required'), Length(min=4, max=25, message='Username must be between 4 and 25 characters')])
    password = PasswordField('Password:', validators=[InputRequired(message='Password required'), Length(min=4, max=25, message='Password must be between 4 and 25 characters')])
    confirm_pswd = PasswordField('Confirm Password:', validators=[InputRequired(message='Password required'), EqualTo('password', message="Passwords must match")])
    submit_button = SubmitField('Create')
