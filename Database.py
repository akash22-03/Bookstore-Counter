Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: E:/Projects/Fantasy Cricket/Database.py ==============
Error in operation.
>>> import sqlite3 as sql
Bookstore = sql.connect('bookstore.db')
cur = Bookstore.cursor()
SyntaxError: multiple statements found while compiling a single statement
>>> import sqlite3 as sql
>>> Bookstore = sql.connect('bookstore.db')
>>> cur = Bookstore.cursor()
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (3,"Celestial Bodies","Jokha Alharthi",123.40);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (8,"Cheque book","Vasdev Mohi",485.36);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>>  cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (9,"The Overstory","Richard Powers",542.20);')
 
SyntaxError: unexpected indent
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (9,"The Overstory","Richard Powers",542.20);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (65,"Bridgital Nation","Viswanathan Anand and Susan Ninan",471.0);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (28,"Manav","Satyarth Nayak",59.90);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (32,"Think Python","Baba Ramdev",69.90);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> cur.execute('INSERT INTO booklib (Count, Name, Author, Price) VALUES (6,"Elements of JAVA","Tridip Suhrud",1132.50);')
<sqlite3.Cursor object at 0x00000153B8D7F570>
>>> Bookstore.commit()
>>> Bookstore.close()
>>> 
