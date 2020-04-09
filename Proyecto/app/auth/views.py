from flask import render_template, session, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm
from app.conexionDB import *
from app.models import *

from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': LoginForm(),
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        
        results = get_user_by_name(username)

        if results[0]['user'] is not None:
            if results[0]['passwrd'] == password:
                user_id = results[0]['user_id']
                user_data = UserData(username, password, user_id)
                user = UserModel(user_data)
                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('hello'))
            else:
                flash('La informacion no coincide')
        else:
            flash('El usuario no existe')

        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))