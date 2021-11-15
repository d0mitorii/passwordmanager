from werkzeug.security import generate_password_hash, check_password_hash
from flask import redirect, url_for, render_template, session

from app import app
from app.models import UserData, Users
from app.database import db
from app.forms import AddPasswordForm, LoginForm, SignupForm


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/')
def home_page():
    if 'user_login' in session:
        return redirect(url_for('index', login=session['user_login']))
    return redirect(url_for('login'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'user_login' in session:
        return redirect(url_for('index', login=session['user_login']))

    error = None
    formLogin = LoginForm()

    if formLogin.validate_on_submit():

        session.pop('user_login', None)

        user = Users.query.filter_by(login=formLogin.login.data).first()

        if not user or not check_password_hash(user.password, formLogin.password.data):
            error = 'Wrong login or password'
        else:
            session['user_login'] = user.login
            return redirect(url_for('index', login=session['user_login']))
        
    return render_template('login.html', form=formLogin, error=error)


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if 'user_login' in session:
        return redirect(url_for('index', login=session['user_login']))

    error = None
    form = SignupForm()

    if form.validate_on_submit():
        
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            error = 'User with this email address exists'
            return render_template('signup.html', form=form, error=error)

        login = Users.query.filter_by(login=form.login.data).first()
        if login:
            error = 'Username is already in use'
            return render_template('signup.html', form=form, error=error)

        hash = generate_password_hash(form.password_repeat.data)
        if not check_password_hash(hash, form.password.data):
            error = 'Password mismatch'
            return render_template('signup.html', form=form, error=error)
        
        try:
            new_user = Users(email=form.email.data,
                             login=form.login.data,
                             password=hash
                             )               
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return 'No added user'
           
    return render_template('signup.html', form=form, error=error)


@app.route("/<login>", methods=['POST', 'GET'])
def index(login):
    if not 'user_login' in session:
        return redirect(url_for('login'))

    if login != session['user_login']:
        return render_template('404.html')

    form = AddPasswordForm()
    user = Users.query.filter_by(login=session['user_login']).first()
    if form.validate_on_submit():
        new_item = UserData(user_id=str(user.id),
                            source=form.source.data,
                            email=form.email.data,
                            login=form.login.data,
                            password=form.password.data
                            )
        try:
            new_item.add()
            return redirect(url_for('index', login=session['user_login']))
        except:
            return 'No added your note'
    else:
        items = UserData.query.filter(UserData.user_id == user.id).all()
        return render_template('index.html', form=form, items=items)


@app.route('/delete/<int:id>')
def delete(id):
    user = Users.query.filter_by(login=session['user_login']).first()
    item_to_delete = UserData.query.get_or_404(id)
    if item_to_delete.user_id != user.id:
        return redirect('/')
    try:
        item_to_delete.delete()
        return redirect('/')
    except:
        return 'No delete'


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))