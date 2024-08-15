from flask_wtf import FlaskForm
from wtforms.validators import Email, Length, DataRequired
from wtforms import PasswordField, StringField, BooleanField, SubmitField
import email_validator
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(2, 64)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(2, 10)])
    remember_me = BooleanField(label='Remember me')
    submit = SubmitField(label='Login')
class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(2, 64)])
    username = StringField(label='Username', validators=[DataRequired(), Length(2, 64)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(2, 10)])
    submit = SubmitField(label='Register')