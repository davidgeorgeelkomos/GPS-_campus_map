import os
import sqlite3


class DB:
    def __init__(self, db_filename ="database.db"):
        self.__db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_filename)
        self.__db_con = sqlite3.connect(self.__db_path)

        # Check if database doesn't exist, create the database
        if not self.__db_con.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall():
            self._create_database()

    def _create_database(self):
        """ Create database tables """
        cur = self.__db_con.cursor()
        cur.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)
        self.__db_con.commit()

    def create_user(self, username, password):
        """ Creates a new user """
        cur = self.__db_con.cursor()
        cur.execute("INSERT INTO users (username,password) VALUES (?,?)", (username,password,))
        self.__db_con.commit()
        return cur.lastrowid

    def get_user(self, username):
        """ Get an existing user """
        """ Query for user info """
        cur = self.__db_con.cursor()
        user = cur.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        return user


    def __del__(self):
        self.__db_con.close()

