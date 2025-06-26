from flask import request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.hashed_password, password):
        session['user_id'] = user.id
        return True
    return False

def logout_user():
    session.pop('user_id', None)

def register_user(username, email, password):
    if User.query.filter_by(username=username).first():
        return False, "Username already exists"
    if User.query.filter_by(email=email).first():
        return False, "Email already registered"
    hashed_pw = generate_password_hash(password)
    user = User(username=username, email=email, hashed_password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return True, "User registered successfully"
