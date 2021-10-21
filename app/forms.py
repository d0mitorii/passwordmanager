from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email

class AddPasswordForm(FlaskForm):
    source = StringField("Source:", validators=[DataRequired()])
    email = StringField("Email:", validators=[Email()])
    login = StringField("Login:")
    password = PasswordField("Password", validators=[DataRequired()])
    add_submit = SubmitField("Add")