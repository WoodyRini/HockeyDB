import mysql.connector
from mysql.connector import Error
 
 
def main():
    """ Connect to MySQL database """
    pw = open('password.txt','r').readline()
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='hockeydb',
                                       user='root',
                                       password=pw)
        cursor = conn.cursor()
        cursor.callproc('test1')
        for result in cursor.stored_results():
            print(result.fetchall())
##        cursor.execute("SELECT * FROM awardsplayers")
        """
        row = cursor.fetchone()


        while row is not None:
            print(row)
            row = cursor.fetchone()
        """
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
 
if __name__ == '__main__':
    main()
