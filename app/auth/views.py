from app.forms import LoginForm
from flask import redirect, render_template, session, flash, url_for

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    context = {
        'login_form': LoginForm()
    }
    login_form = LoginForm()

    if login_form.validate_on_submit():
        session['username'] = login_form.username.data

        flash('User created successfully')
        return redirect(url_for('index'))

    return render_template('login.html', **context)
