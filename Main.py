import sqlite3 as sql
Bookstore = sql.connect('bookstore.db')
cur = Bookstore.cursor()
tcost = 0
while True:
    name = input('Book Title: ')
    sql = 'SELECT * FROM booklib WHERE Name == "'+name+'";'
    cur.execute(sql)
    record = cur.fetchone()
    if record==None:
        break
    print(record)
    copy = int(input("No. of Copies: "))
    if copy > record[0]:
        print("Not enough copies available")
        continue
    tcost = tcost + record[3]*copy
    curcount = record[0] - copy
    sql1 = 'UPDATE booklib SET Count = "'+str(curcount)+'" WHERE Name == "'+name+'";'
    cur.execute(sql1)
    next = input("Add more books?(Y/N): ")
    if(next=='N'):
        break
    Bookstore.commit()
    
print("Total Cost: "+str(tcost))
Bookstore.close()
