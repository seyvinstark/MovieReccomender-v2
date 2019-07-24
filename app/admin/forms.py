from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Genre


class GenreForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MovieForm(FlaskForm):
    """
    Form for admin to add movie
    """

    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    genre = StringField('Category', validators=[DataRequired()])


    rating = IntegerField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')
