import mysql.connector
from mysql.connector import Error
 
 
def main():
    """ Connect to MySQL database """
    ## draws password from a local text file.
    pw = open('password.txt','r').readline()
    storedProcResults = []
    queryResults = []
    ## Find the results of these queries in the output.txt file as created below.
    outfile = open('output.txt','w')
    ## an empty list to show python aggregation - total abelsi postseason wins - calculated at end of script. Displayed at very end of output file.
    abelsirecords = []
    abelsipostwins = 0
    
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='hockeydb',
                                       user='root',
                                       password=pw)
        cursor = conn.cursor()
        
        
        cursor.callproc('sortPlayersByAwards')

        for result in cursor.stored_results():
            storedProcResults.append(result.fetchall())
            
        cursor.execute("SELECT * FROM coaches where coachID = 'abelsi01c'")
        row = cursor.fetchone()

        
        while row is not None:
            abelsirecords.append(row)
            row = cursor.fetchone()

        cursor.execute("select coachID, year, w from `hockeydb`.`coaches` order by year, w desc")
        row = cursor.fetchone()
        
        while row is not None:
            queryResults.append(row)
            row = cursor.fetchone()
            
    except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()

    ## grab the non-null win records for this coach and aggregate them with integer addition.
    for year in abelsirecords:
        if year[11] != '':
            abelsipostwins+= int(year[11])
            
## write the output to a file.
    outfile.write(str(storedProcResults))
    outfile.write(str(queryResults))
    outfile.write(str(abelsipostwins))
 
if __name__ == '__main__':
    main()
