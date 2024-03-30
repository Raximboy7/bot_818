import psycopg2
from config import *

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database=DB_NAME,
            password=DB_PASSWORD,
            user=DB_USERS,
            host=DB_HOST
        )

    def execute_query(self, sql, *args, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()

    def create_users_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users (
             id SERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE,
            fullname VARCHAR(40),
            birthdate DATE,
            contact VARCHAR(20) UNIQUE
        )'''
        self.execute_query(sql, commit=True)

    def users_list(self):
        sql = '''SELECT telegram_id FROM users'''
        return self.execute_query(sql, fetchall=True)

    def insert_user(self, telegram_id, fullname, age, contact):
        sql = '''INSERT INTO users VALUES(%s, %s, %s, %s, %s)'''
        self.execute_query(sql, (telegram_id, fullname, age, contact), commit=True)

    def insert_user_id(self, telegram_id):
        sql = '''INSERT INTO users(telegram_id) VALUES (%s) ON CONFLICT DO NOTHING'''
        self.execute_query(sql, (telegram_id,), commit=True)

    def check_user(self, telegram_id):
        sql = '''SELECT * FROM users WHERE telegram_id = %s'''
        return self.execute_query(sql, (telegram_id,), fetchone=True)

    def save_user(self, fullname, birthdate, contact, telegram_id):
        sql = '''UPDATE users SET fullname=%s, birthdate=%s, contact=%s WHERE telegram_id=%s'''
        self.execute_query(sql, (fullname, birthdate, contact, telegram_id), commit=True)

