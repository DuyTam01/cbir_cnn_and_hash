from website import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(120))
    # relationship with Posttable(1-n)
    posts = db.relationship('Post', backref="author", lazy="dynamic")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return "<User %s>" % self.username
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    image_url = db.Column(db.String(140))
    categorical = db.Column(db.String(50), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    # relationship (n-1) with User table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Post %s>" % self.title
