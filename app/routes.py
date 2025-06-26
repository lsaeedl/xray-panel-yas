from flask import Blueprint, render_template, request, redirect, url_for, session
from . import db
from .models import User

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("dashboard.html")

# ادامه مسیرها در مراحل بعدی
