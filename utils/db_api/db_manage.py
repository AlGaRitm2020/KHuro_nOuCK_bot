import sqlite3
con = sqlite3.connect('books.db')

cur = con.cursor()
#cur.execute("drop table favorites;")
#cur.execute("drop table users")

#cur.execute("create table users( username VARCHAR, chat_id INTEGER PRIMARY KEY unique);")
"""
cur.execute("drop table books;")
cur.execute("drop table favorites;")
cur.execute("create table users(id serial primary key, username VARCHAR, chat_id  VARCHAR unique);")

cur.execute("create table books(id serial primary key, book_name VARCHAR);")
"""
#cur.execute("create table favorites(chat_id INTEGER references users,  book_name VARCHAR , is_read INTEGER, rate INTEGER, feedback VARCHAR);")

#cur.execute("INSERT INTO favorites (chat_id, book_name, is_read, rate, feedback) VALUES (1830477841, 'Введение в алгебру. В 3-х частях. Часть 2. Линейная алгебра', 1, 8,'Лучшая книга по алгебре. Очень рекомендую' )")
#cur.execute("create table rates(chat_id INTEGER references users,  book_name VARCHAR primary key, rate INTEGER);")

#cur.execute("create table folders(chat_id INTEGER references users,  book_name VARCHAR , folder VARCHAR);")
cur.execute("select * from users")
print(cur.fetchall())




#cur.execute("INSERT INTO favorites (chat_id, book_name, is_read, rate, feedback) VALUES (1830477841, 'Введение в алгебру. В 3-х частях. Часть 2. Линейная алгебра', 1, 8,'Лучшая книга по алгебре. Очень рекомендую' )")
#cur.execute("UPDATE favorites SET is_read = 1")
cur.execute("select * from favorites")
print(cur.fetchall())


