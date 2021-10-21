from flask import request, redirect, url_for, render_template
from wtforms.validators import Email

from app import app
from app.models import PasswordManager
from app.database import db
from app.forms import AddPasswordForm


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