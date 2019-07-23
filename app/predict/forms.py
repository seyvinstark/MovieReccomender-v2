from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class MovieForm(FlaskForm):
    '''
    form where the user put in a movie to see if we have it
    '''
    movie_entered = StringField('Enter a Movie', validators=[DataRequired()])
    submit = SubmitField('Submit')#no validation errors yet

