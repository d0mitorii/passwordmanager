import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, render_template, session, g

from app import app
from app.models import PasswordManager, Users
from app.database import db
from app.forms import AddPasswordForm, LoginForm, RegistrationForm


@app.before_request
def before_request():
    g.user = None

    if 'user_login' in session:
        user = Users.query.filter_by(login=session['user_login']).first()
        g.user = user


@app.route("/login", methods=['POST', 'GET'])
def login():
    session.pop('user_login', None)
    formLogin = LoginForm();
    if formLogin.validate_on_submit():

        session.pop('user_login', None)

        user = Users.query.filter_by(login=formLogin.login.data).first()

        # if user.password == generate_password_hash(formLogin.password.data):
        #     session['user_login'] = user.login

        if user.password == formLogin.password.data:    # Изменить проверку пароля
            session['user_login'] = user.login
            return redirect(url_for('index', login=user.login))

    return render_template('login.html', formLogin=formLogin)


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    form = RegistrationForm();
    if form.validate_on_submit():
        
        user = Users.query.filter_by(email=form.email.data).first()

        if user:
            return redirect(url_for('login'))

        login = Users.query.filter_by(login=form.login.data).first()

        if login:
            return 'login est'

        # hash = generate_password_hash(form.password.data) 
        # hash1 = generate_password_hash(form.password_repeat.data)
        # print(hash)
        # print(hash1)
        # if not check_password_hash(hash, generate_password_hash(form.password_repeat.data)):
        #     return 'Passwords ne sowpadayut'

        if form.password_repeat.data != form.password.data: # Изменить проверку пароля
            return 'Passwords ne sowpadayut'

        try:
            new_user = Users(email=form.email.data,
                            login=form.login.data,
                            password=form.password.data)    # Изменить проверку пароля
                            # password=hash)                
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'No added user'
    return render_template('registration.html', formRegistration=form)


@app.route("/<login>", methods=['POST', 'GET'])
def index(login):

    if not g.user:
        return redirect(url_for('login'))

    form = AddPasswordForm()
    if form.validate_on_submit():
        new_item = PasswordManager(user_login=str(g.user.login),
                                   source=form.source.data,
                                   email=form.email.data,
                                   login=form.login.data,
                                   password=form.password.data)
        try:
            new_item.add()
            return redirect(url_for('index', login=login))
        except:
            return 'No added your note'
    else:
        items = PasswordManager.query.filter(PasswordManager.user_login == g.user.login).all()
        return render_template('index.html', form=form, items=items)


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = PasswordManager.query.get_or_404(id)
    try:
        item_to_delete.delete()
        return redirect('/')
    except:
        return 'No delete'