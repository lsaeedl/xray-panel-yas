import os
from datetime import datetime

BACKUP_DIR = "/opt/xray-panel/backups"
DB_NAME = "xraypanel"
DB_USER = "postgres"

def create_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"{DB_NAME}_backup_{now}.sql")
    cmd = f"pg_dump -U {DB_USER} {DB_NAME} > {backup_path}"
    os.system(cmd)
    print(f"✅ بکاپ با موفقیت در مسیر {backup_path} ذخیره شد.")

if __name__ == "__main__":
    create_backup()
