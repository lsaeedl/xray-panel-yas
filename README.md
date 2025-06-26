# xray-panel-yas
# پروژه مدیریت Xray + Reality با پنل وب و ربات تلگرام

**کاربر:** سعید سراوانی  
**ایمیل:** xsecurityx@gmail.com  
**دامنه پنل:** https://panel.misyas.com  
**سیستم عامل:** Ubuntu 24.04  
**زبان برنامه‌نویسی:** Python (Flask)  
**دیتابیس:** PostgreSQL  
**وضعیت توسعه:** فعال

---

## پیش‌نیازها

- سرور Ubuntu 24.04  
- Python 3.11+  
- PostgreSQL 15+  
- Nginx  
- دامنه‌های تنظیم شده روی Cloudflare  
- توکن ربات تلگرام (BotFather)  
- API Key NowPayments  

---

## ساختار پروژه

xray-panel-yas/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── auth.py
│ ├── config.py
│ ├── utils.py
│ ├── backup.py
│ └── templates/
├── bot/
│ ├── bot.py
│ └── handlers.py
├── scripts/
│ ├── add_user.py
│ ├── remove_user.py
│ ├── reset_traffic.py
│ └── backup_db.py
├── migrations/
├── tests/
├── requirements.txt
├── config.env
├── run.py
├── .gitignore
└── README.md


---

## راه‌اندازی اولیه

### 1. کلون کردن پروژه

```bash
git clone https://github.com/lsaeedl/xray-panel-yas.git
cd xray-panel-yas
2. نصب وابستگی‌ها
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. تنظیم متغیرهای محیطی (config.env)
env
Copy
Edit
SECRET_KEY=کلید_امن_شما
DB_URL=postgresql://user:password@localhost:5432/xray_db
TELEGRAM_BOT_TOKEN=توکن_ربات_شما
NOWPAYMENTS_API_KEY=کلید_پرداخت
DOMAIN_BASE=misyas.com
4. ایجاد دیتابیس
sql
Copy
Edit
sudo -u postgres psql
CREATE DATABASE xray_db;
CREATE USER xray_user WITH PASSWORD 'رمزعبور';
GRANT ALL PRIVILEGES ON DATABASE xray_db TO xray_user;
\q
5. مهاجرت دیتابیس
bash
Copy
Edit
flask db init
flask db migrate -m "initial migration"
flask db upgrade
6. اجرای برنامه
bash
Copy
Edit
python run.py
پیکربندی Nginx
nginx
Copy
Edit
server {
    listen 80;
    server_name panel.misyas.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
راه‌اندازی ربات تلگرام
bash
Copy
Edit
cd bot
python bot.py
اسکریپت‌های مدیریتی
افزودن کاربر:
python scripts/add_user.py

حذف کاربر:
python scripts/remove_user.py

ریست ترافیک کاربر:
python scripts/reset_traffic.py

بکاپ دیتابیس:
python scripts/backup_db.py

امکانات کلیدی
مدیریت کاربران از طریق وب و ربات

پرداخت امن با ارز دیجیتال (NowPayments)

لینک اشتراک امن با توکن اختصاصی

مدیریت چند سرور و Failover

محدودیت اتصال همزمان

بکاپ و بازیابی دیتابیس و فایل‌های پیکربندی از پنل

نمایش آمار و مصرف کاربران

هشدار مصرف از طریق ربات تلگرام

پشتیبانی و ارتباط
ایمیل: xsecurityx@gmail.com

ریپازیتوری GitHub: https://github.com/lsaeedl/xray-panel-yas

توسعه‌های آینده
درگاه پرداخت ریالی

داشبورد گرافیکی پیشرفته

اپ موبایل

چندزبانه

API عمومی

این پروژه تحت توسعه مداوم است و هرگونه به‌روزرسانی در ریپازیتوری اطلاع‌رسانی خواهد شد.
