from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
    category = QuerySelectField(query_factory=lambda: Genre.query.all(),
                                  get_label="name")

    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')
