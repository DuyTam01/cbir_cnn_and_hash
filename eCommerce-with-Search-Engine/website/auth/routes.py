from website.auth import bp
from flask import render_template, url_for, redirect, flash
from flask_login import login_required, current_user, login_user, logout_user
from website.auth.forms import LoginForm, RegisterForm
from website.models import User
from website import db
@bp.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Email or password invalid')
            return redirect(url_for('auth.login'))
        login_user(user=user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)
@bp.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Registered email, please use another email.')
            return redirect(url_for('auth.register'))
        user = User(email=form.email.data, username=form.username.data)
        user.set_password(password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered successfully, Welcome %s.' % form.username.data)
        login_user(user=user)
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('See you yah!')
    return redirect(url_for('auth.login'))