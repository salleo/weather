from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class EnterTown(Form):

    name = StringField('town_name', validators=[DataRequired()])

