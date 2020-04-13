from flask import render_template, session, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user

from werkzeug.security import generate_password_hash, check_password_hash

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
        
        results, flag = get_user_by_name(username)

        if flag:
            if results[0]['passwrd'] == password:
                user_id = results[0]['user_id']
                user_data = UserData(username, password, user_id)
                user = UserModel(user_data)
                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('hello'))
            else:
                flash('La informacion no coincide')
                flash(results[0]['passwrd'])
        else:
            flash('El usuario no existe')

        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = LoginForm()

    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        results, flag = get_user_by_name(username)

        if flag is False:
            password_hash = generate_password_hash(password)

            new_user(username, password)

            results, flag = get_user_by_name(username)

            user_data=UserData(results[0]['user'],results[0]['passwrd'],results[0]['user_id'])

            user = UserModel(user_data)

            login_user(user)

            flash('Bienvenido')

            return redirect(url_for('index'))

        else:
            flash('el Usuario ya existe')

    return render_template('signup.html', **context)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))