from . import db
from flask_login import UserMixin
from . import login

class User(UserMixin, db.Model):
    '''User model'''
    
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    def __repr__(self):
        return f'User {self.username}'

@login.user_loader
def load_user(id):
   return User.query.get(int(id))