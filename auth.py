from flask import Blueprint, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from models import User
from werkzeug.security import check_password_hash

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('main_routes.home'))
        flash('Login inválido')
    return "Página de Login"

@auth_routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_routes.login'))