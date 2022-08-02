from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_all
from flask_login import login_required, current_user

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    context = {
        'code': 404,
        'message_for_error': 'Not Found',
        'error': error
    }
    return render_template('/http_error.html', **context)


@app.errorhandler(500)
def internal_server_error(error):
    context = {
        'code': 500,
        'message_for_error': 'Internal Server Error',
        'error': error
    }
    return render_template('/http_error.html', **context)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response


all = ['Todo 1', 'Todo 2', 'Todo 3', 'Todo 4']


@app.route('/hello', methods=['GET'])
@login_required
def hello():
    # user_ip = request.cookies.get("user_ip")
    user_ip = session.get('user_ip')
    # username = session.get('username')
    username = current_user.id
    alls = get_all(username)

    context = {
        'user_ip': user_ip,
        'all': alls,
        'username': username
    }

    return render_template('hello.html', **context)
