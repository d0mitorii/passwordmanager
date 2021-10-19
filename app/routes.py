from app import app
from app.models import PasswordManager
from app.database import db
from flask import request, redirect, url_for, render_template


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_sourse = request.form['source']
        item_email = request.form['email']
        item_login = request.form['login']
        item_password = request.form['password']
        if item_sourse == '' and item_email == '' and item_password== '' :
            return 'No input'
        new_item = PasswordManager(source=item_sourse, email=item_email, login=item_login, password=item_password)
        
        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'No added your note'
    else:
        items = PasswordManager.query.order_by(PasswordManager.id).all()
        return render_template('index.html', items=items)


@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = PasswordManager.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'No delete'