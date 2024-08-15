from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SelectField, SubmitField
from wtforms.validators import Length, DataRequired
categoricals = ['tmp1', 'tmp2']
class PostForm(FlaskForm):
    title = TextAreaField(label='Title', validators=[Length(min=1, max=150)])
    image_url = StringField(label='Image url', validators=[DataRequired()])
    categorical = SelectField(label='Categorical', choices=categoricals)
    submit = SubmitField(label='Post')