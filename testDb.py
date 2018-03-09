import sqlite3

db_name = "athletes"


class testdb:
    def __init__(self):
        pass

    def insert(self, name="zz", dob="dd"):
        connection = sqlite3.connect("coachdata.sqlite")
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS """ + db_name + """(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL ,
        name TEXT NOT NULL ,
        dob DATA NOT NULL )""")
        cursor.execute("INSERT INTO " +db_name + "(name ,dob) VALUES (?,?)", (name, dob))
        connection.commit()
        connection.close()
        


testdb().insert()
