from crypt import methods
import email
from ensurepip import bootstrap
from multiprocessing import context
from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRET'
bootstrap = Bootstrap(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    surnames = StringField('Surnames', validators = [DataRequired()])
    email = EmailField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    context = {
        'code': 404,
        'message_for_error' : 'Not Found',
        'error' : error
    }
    return render_template('/http_error.html', **context)

@app.errorhandler(500)
def internal_server_error(error):
    context = {
        'code': 500,
        'message_for_error' : 'Internal Server Error',
        'error' : error
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
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get("user_ip")
    user_ip = session.get('user_ip')

    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'all' : all,
        'login_form' : login_form
    }
    return render_template('/hello.html', **context)