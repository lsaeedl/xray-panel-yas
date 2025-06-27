from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#اجرای پروژه Flask
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

from flask_migrate import Migrate
from app import app, db  # فرض اینکه app و db قبلاً تعریف شده‌اند

migrate = Migrate(app, db)


