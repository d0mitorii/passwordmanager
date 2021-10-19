from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    login = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.id


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

if __name__ == '__main__':
    app.run(debug=True)