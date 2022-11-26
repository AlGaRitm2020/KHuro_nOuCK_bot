import sqlite3


async def register(username, chat_id):
    con = sqlite3.connect('books.db')
    cur = con.cursor()

    check_request = "SELECT * FROM users WHERE chat_id = '{}'".format(str(chat_id))
    cur.execute(check_request)
    users_with_this_id = cur.fetchall()
    if len(users_with_this_id):
        return False
    insert_request = "INSERT INTO users(username, chat_id) VALUES('{}', '{}' )". \
        format(username, chat_id)
    cur.execute(insert_request)
    con.commit()
    return True

async def add_to_favorites(book_name, chat_id):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    """ 
    request = "SELECT * FROM users WHERE chat_id = '{}'".format(str(chat_id))
    cur.execute(request)
    user_id = cur.fetchall()
    if not len(user_id):
        print('user isn"t exist')
        return False
"""
    print("BOOOK NAME           ", book_name)
    check_request = "SELECT * FROM favorites WHERE chat_id= {} AND book_name = '{}'".format(chat_id, book_name)
    cur.execute(check_request)
    res = cur.fetchall()
    
    if (len(res) == 0):
        cur.execute("INSERT INTO favorites (book_name, chat_id, is_read, rate, feedback) VALUES ('{}', {}, {}, {}, '{}')".format(book_name, chat_id, 0, 0, "")) 

    con.commit()
    return True

async def get_favorites(chat_id):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
    
    cur.execute("SELECT book_name, is_read, rate, feedback from favorites WHERE chat_id= {} ;".format(chat_id)) 
    res = cur.fetchall()
    con.commit()
    


    return res 

async def make_rate(chat_id, book_name, rate):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
     
    cur.execute("SELECT rate from favorites WHERE chat_id= {} AND book_name ='{}' ;".format(chat_id, book_name)) 
    res = cur.fetchall()
    if (len(res) == 0):
        cur.execute("INSERT INTO favorites (book_name,is_read chat_id, rate, feedback) VALUES ('{}',{}, {}, {}, '{}')".format(book_name,0, chat_id, rate, '')) 
    else:
        cur.execute("UPDATE favorites SET rate = '{}' WHERE chat_id = '{}' AND book_name = '{}'".format(rate, chat_id, book_name))


    con.commit()
    return True


async def make_feedback(chat_id, book_name, feedback):
    con = sqlite3.connect('books.db')
    cur = con.cursor()

    cur.execute("SELECT feedback from favorites WHERE chat_id= {} AND book_name ='{}' ;".format(chat_id, book_name)) 
    res = cur.fetchall()
    if (len(res) == 0):
        cur.execute("INSERT INTO favorites (book_name, chat_id,is_read, rate, feedback) VALUES ('{}',{}, {}, {}, '{}')".format(book_name, chat_id,0, 0,feedback)) 
    else:
        cur.execute("UPDATE favorites SET feedback = '{}' WHERE chat_id = '{}' AND book_name = '{}'".format(feedback, chat_id, book_name))

    con.commit()


async def get_average_rate(book_name):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
     
    cur.execute("SELECT rate from favorites WHERE book_name ='{}' ;".format(book_name)) 
    

    res = []
    fetch = cur.fetchall()
    if (len(fetch)!=0):
        for i in fetch:
            res.append(i[0]) 
    
        avg = sum(res) / len(res)
        return avg

    return 0.0

async def get_feedbacks(book_name):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
     
    cur.execute("SELECT feedback, rate, chat_id from favorites WHERE book_name ='{}' ;".format(book_name)) 
    

    res = []
    fetch = cur.fetchall()
    if (len(fetch)!=0):
        for i in fetch:
            res.append((i[0],i[1], i[2]) ) 
    return res 

async def change_is_read(book_name, chat_id):
    con = sqlite3.connect('books.db')
    cur = con.cursor()
     
    cur.execute("SELECT is_read from favorites WHERE book_name ='{}' AND chat_id = {};".format(book_name, chat_id)) 
    is_read = cur.fetchall()
    if (len(is_read)==0):
        return False
    is_read = is_read[0][0]
            

    cur.execute("UPDATE favorites SET is_read = '{}' WHERE chat_id = '{}' AND book_name = '{}'".format((is_read+1) % 2, chat_id, book_name))


    con.commit()




