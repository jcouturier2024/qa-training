# Suggested code may be subject to a license. Learn more: ~LicenseLog:3980885671.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1038937557.
import sqlite3

def create_database():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def print_databse()
