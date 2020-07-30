import sqlite3

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def view_all(self):
        self.cursor.execute("SELECT * from book")
        results = self.cursor.fetchall()
        return results

    def insert(self, title, author, year, isbn):
        self.cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cursor.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()

    def search(self, title="", author="",year="",isbn=""):
        self.cursor.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        results = self.cursor.fetchall()
        return results

    # def find_by_id(id):
    #     conn = sqlite3.connect("books.db")
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * from book WHERE id=?",(id,))
    #     results = cursor.fetchone()
    #     conn.close()
    #     return results

    def __del__(self):
        self.conn.close