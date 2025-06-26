#!/bin/bash

echo "==============================================="
echo "💡 نصب خودکار xray-panel-yas روی Ubuntu 24.04"
echo "==============================================="

read -p "📌 نام دیتابیس PostgreSQL (مثلاً xray_panel): " DB_NAME
read -p "👤 نام کاربری دیتابیس PostgreSQL: " DB_USER
read -s -p "🔐 رمز عبور کاربر PostgreSQL: " DB_PASS
echo

# 1. نصب پیش‌نیازها
echo "✅ نصب وابستگی‌های سیستم..."
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib libpq-dev build-essential git

# 2. ساخت دیتابیس و یوزر PostgreSQL
echo "📦 ساخت دیتابیس و یوزر در PostgreSQL..."
sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'Asia/Tehran';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

# 3. نصب پروژه
PROJECT_DIR=~/xray-panel-yas
if [ ! -d "$PROJECT_DIR" ]; then
  echo "📥 کلون پروژه از گیت‌هاب..."
  git clone https://github.com/lsaeedl/xray-panel-yas.git $PROJECT_DIR
fi

cd $PROJECT_DIR

# 4. ساخت محیط مجازی و نصب پکیج‌ها
echo "⚙️ ایجاد محیط مجازی پایتون..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 5. تنظیم متغیر محیطی
export DATABASE_URL=postgresql://$DB_USER:$DB_PASS@localhost:5432/$DB_NAME
export FLASK_APP=run.py

# 6. اجرای مهاجرت دیتابیس
echo "📂 اجرای مهاجرت دیتابیس..."
flask db upgrade

# 7. اجرای برنامه
echo "🚀 اجرای برنامه Flask..."
flask run --host=0.0.0.0 --port=5000
