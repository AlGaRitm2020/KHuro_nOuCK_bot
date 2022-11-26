import sqlite3
con = sqlite3.connect('books.db')

cur = con.cursor()

cur.execute("create table users(id serial primary key, username VARCHAR, chat_id  VARCHAR unique);")
cur.execute("create table books(id serial primary key, book_name VARCHAR);")
cur.execute("create table favorites(id serial primary key, user_id INTEGER references users,  book_id INTEGER references books, is_read);")

cur.execute("create table stats(id serial primary key, user_id INTEGER references users, task_num INTEGER, right_answers INTEGER, all_answers INTEGER);")




print(cur.fetchall())
