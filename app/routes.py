from flask import Blueprint, render_template, request, redirect, url_for, session
from . import db
from .models import User

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("dashboard.html")

# ادامه مسیرها در مراحل بعدی
from flask import request, session, redirect, url_for, render_template, flash
from .auth import login_user, logout_user, register_user

@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if login_user(username, password):
            return redirect(url_for("main.index"))
        else:
            flash("نام کاربری یا رمز اشتباه است")
    return render_template("login.html")

@main_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.login"))

@main_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        success, msg = register_user(username, email, password)
        if success:
            flash("ثبت‌نام با موفقیت انجام شد. اکنون وارد شوید.")
            return redirect(url_for("main.login"))
        else:
            flash(msg)
    return render_template("register.html")
