from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    subscription_token = db.Column(db.String(256), unique=True)
    traffic_used = db.Column(db.BigInteger, default=0)
    traffic_limit = db.Column(db.BigInteger, nullable=True)  # Null = unlimited
    expire_date = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
