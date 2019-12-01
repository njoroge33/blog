from . import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash
from . import login
import arrow
from sqlalchemy.orm import relationship

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

    def verify_password(self,password):
        return check_password_hash(self.password,password)

@login.user_loader
def load_user(id):
   return User.query.get(int(id))

class Blog(db.Model):
    '''Blog model'''
    
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    user = relationship("User", backref="Blog")
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    date = db.Column(db.DateTime, nullable=False, default=arrow.utcnow().datetime)

    def __repr__(self):
        return f'Blog {self.description}'
    

    @classmethod
    def get_blogs(cls,owner_id):
        blogs = Blog.query.filter_by(owner_id=owner_id).all()
        return blogs

class Quote:
    '''Quotes model'''

    def __init__(self,author,id,quote,permalink):
        self.author =  author
        self.id =id
        self.quote = quote
        self.permalink = permalink

class Comment(db.Model):
    '''Comments model'''
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    user = relationship('User', backref='Comment')
    description = db.Column(db.Text)
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"
