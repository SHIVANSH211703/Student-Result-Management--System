import sqlite3

def create_db():
    con = sqlite3.connect("rms.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            duration TEXT,
            charges TEXT,
            description TEXT
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
                name text,
                 email text ,
                  gender text, 
                 dobtext , 
                contact text ,
                 addmission text , 
                course text ,
                 state text,
                 city text ,
                 pin text,
                 address text 
            
        )
    """)
     
    con.commit()
    con.close()

create_db()
