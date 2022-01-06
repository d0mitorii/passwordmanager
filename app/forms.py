from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class AddPasswordForm(FlaskForm):
    source = StringField("source", validators=[DataRequired()])
    email = StringField("email", validators=[Email()])
    login = StringField("login")
    password = PasswordField("password", validators=[DataRequired()])
    add_submit = SubmitField("Add")
    upd_submit = SubmitField("Upd")


class LoginForm(FlaskForm):
    login = StringField("login", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    login_submit = SubmitField("Login")


class SignupForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email()])
    login = StringField("login", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    password_repeat = PasswordField("repeat password", validators=[DataRequired()])
    signup_submit = SubmitField("Sign Up")