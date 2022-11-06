import MySQLdb
import MySQLdb.cursors


conn = None

def get_db():
    global conn

    if conn is None:
        conn = MySQLdb.connect(
            host="localhost", 
            user="root",
            passwd="Ambra11erla", 
            db="blog", 
            cursorclass=MySQLdb.cursors.DictCursor
        )
    
    return conn