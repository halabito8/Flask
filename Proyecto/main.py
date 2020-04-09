import unittest
from flask import request, redirect, make_response, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.forms import LoginForm
from app.conexionDB import *

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/res')
def res():
    results = get_todos(user_id=1)
    return results[0]['todo']


@app.route('/usuarios')
def usuarios():
    results = get_users()
    return results[0]['user']

@app.route('/usuario')
def usuario():
    results = get_user_by_name(user='david')
    return results[0]['passwrd']
    

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip']=user_ip

    return response


@app.route('/hello', methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.user
    # login_form = LoginForm()
    # username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todo': get_todos(user_id=1),
        # 'login_form': login_form,
        'username': username,
    }

    # if login_form.validate_on_submit():
    #     username = login_form.username.data
    #     session['username'] = username

    #     flash('Nombre de usuario registrado con exito')

    #     return redirect(url_for('index'))

    return render_template('hello.html', **context)