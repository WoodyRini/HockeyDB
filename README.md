# HockeyDB
A Hockey database for querying coaches, players, and awards.
This database is designed to demonstrate:
- Knowledge of SQL
- Python data processing
- Ability to work with Git and GitHub

This Repository contains the following:
1) Three CSV files from an open source hockey DB http://www.opensourcesports.com/hockey/ to work with a database
2) A mainScript.py file - This file can run queries, aggregate data, and write the output to a text file.
3) A Schema File - this can be used to replicate the schema for my databases in mySQL if you'd like.
4) a "createSchemaFile.py" file - this python file can generate a schema based on the opensourcesports.com tables you'd like to use. Just remember to add keys and modify data types if you want to use this!
5) A query file that contains the SQL for my stored procedure and query, in case you want to use it in the mySQL workbench. 

To Replicate my work, do the following:
1) Make sure you have local mySQL setup with the python connector! Clone this code to a local repository.
2) Open the mySQL workbench, create an editor, copy the HockeyDBSchemaFile text into the editor, and run it. This should create your schema and tables. If you want to use the createSchemaFile.py code instead, you can run that and it'll generate the file for you. Just make sure to change the coach table's "w" column to int if you want accurate results for my queries.
3) Copy the Stored procedure from Query1andStoredProc file and run the sql. This will create your stored procedure.
4) Create a file called password.txt in the same directory as this code and as the first and only line, enter your mySQL root user password (This is to mask the password while still being able to parameterize and script the database connection in python).
5) Run "mainScript.py"! This will connect to the db, run the query, stored proc, and aggregation, and write those results to a file.
5b) If you wish, copy the queries and run them in the workbench to view the results there.
6) Check your output file for results! And you can take advantage of that script to code in some more queries if you'd like, making things easy to run fast. Same for creating a different schema.

Improvements needed with time:
- Never created the third query, linking player with most awards in a season to coach whose team had the most wins, because I couldn't find a link between player and team in the database. Is this an oversight on my part?
- Scripting is rudimentary in a few ways. One, if we also scripted executing the schema and creating the stored proc, we wouldn't need the workbench. Two, the output file handles unicode in a pretty ugly fashion - we could certainly make this output look a lot more readable with time.

