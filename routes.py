from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from extensions import db
from models import User
from forms import LoginForm, SignupForm

routes = Blueprint('routes', __name__)

@routes.route('/terms')
def terms():
    return render_template('terms.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        if not form.accept_terms.data:
            flash('이용약관에 동의해야 회원가입이 가능합니다.', 'danger')
            return redirect(url_for('routes.signup'))

        user = User(username=form.username.data, email=form.email.data, terms_accepted=True)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('회원가입 완료! 이제 로그인하세요.', 'success')
        return redirect(url_for('routes.login'))
    return render_template('signup.html', form=form)

@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('로그인 성공!', 'success')
            return redirect(url_for('routes.dashboard'))
        flash('이메일 또는 비밀번호가 잘못되었습니다.', 'danger')
    return render_template('login.html', form=form)

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('로그아웃 완료.', 'info')
    return redirect(url_for('routes.login'))

@routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username, credits=current_user.credits)
