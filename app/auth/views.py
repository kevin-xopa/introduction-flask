from tkinter import E
import flask
from app.forms import LoginForm
from flask import redirect, render_template, session, flash, url_for
from flask_login import login_user, login_required, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth
from app.firestore_service import get_user, user_put
from app.models import UserModel, UserData


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    context = {
        'login_form': LoginForm()
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = get_user(username)

        if user.to_dict() is not None:
            password_from_db = user.to_dict()["password"]
            if password_from_db == password:
                user_data = UserData(username, password)
                user_model = UserModel(user_data)
                login_user(user_model)

                flash('Bienvenido')
                redirect(url_for("hello"))
            else:
                flash('Las credenciales son incorrectas')
        else:
            flash('Usuario no encontrado')

        return redirect(url_for('index'))

    return render_template('login.html', **context)


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    signup_form = LoginForm()

    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        user = get_user(username)
        if user.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)
            login_user(user)

            flash("Bienvenido!!!...")

            return redirect(url_for('hello'))
        else:
            flash('Usuario existente')

    return render_template('signup.html', **context)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Adiosito')

    return redirect(url_for('auth.login'))
