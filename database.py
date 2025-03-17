 
import mysql.connector
from settings import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    if conn.is_connected():
        print("✅ MySQL-ga muvaffaqiyatli ulandik!")
except mysql.connector.Error as e:
    print(f"❌ MySQL ulanishida xatolik: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()