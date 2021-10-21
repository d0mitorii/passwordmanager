from operator import methodcaller
from flask import request, redirect, url_for, render_template
from wtforms import form
from wtforms.validators import Email

from app import app
from app.models import PasswordManager
from app.database import db
from app.forms import AddPasswordForm, Login

@app.route("/login", methods=['POST', 'GET'])
def login():
    formLogin = Login();
    if formLogin.validate_on_submit():
        return redirect('/')
    return render_template('login.html', form=formLogin)


@app.route("/", methods=['POST', 'GET'])
def index():
    form = AddPasswordForm()
    if form.validate_on_submit():
        new_item = PasswordManager(source=form.source.data,
                                   email=form.email.data,
                                   login=form.login.data,
                                   password=form.password.data)
        try:
            new_item.add()
            return redirect('/')
        except:
            return 'No added your note'
    else:
        items = PasswordManager.query.order_by(PasswordManager.id).all()
        return render_template('index.html', form=form, items=items)


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = PasswordManager.query.get_or_404(id)
    try:
        item_to_delete.delete()
        return redirect('/')
    except:
        return 'No delete'