# -*- coding: utf-8 -*-
"""
@Created by Woody Rini 2017.

A Python file to create mySQL Schemas for any customized set of tables from a database.
1) Download and Extract to your directory the desired CSV files from http://www.opensourcesports.com/ (I used hockey)
2) Copy this file to the same directory as those CSV files.
3) Modify the "tableNames" variable below to list the tables you'd like to create the schema file for, and the "schema" variable to your schema name.
4) Run this script
5) Manually modify the data type (script automatically creates varchar(30)) for each column - choose based on your own logic.
6) Add your key contraints and not nulls as you see fit
7) Run the script in mySQL to create your Schema and Tables!

Future functionality: Read the entire table in, profile the data in python, and make type and character length recommendations based on that? This would be critical to resolve bugs for example, sorting by # of wins, because as a character wins will be sorted differently!!

"""

import csv


def main():
    
    ## open a new file to store our generated schema file - modify name as desired for a different db.
    schema = "hockeydb"
    schemaFile = open(schema + "SchemaFile.txt","w")
    ## MODIFY THE LINE BELOW - this is the list of tables you want to include in the schema.
    tableNames = ["Master","AwardsPlayers","Coaches"]
    ## begin creating a text block that will become our full schema creation SQL statement.
    schemaFileText = "Create Schema `" + schema + "` \n"
    ## iterate through the tables we want to create. For each one, use the column names from the first row and python text formatting to make a "Create Table" file.
    for i in range(len(tableNames)):
        schemaFileText += "Create Table `" + schema + "`.`" + tableNames[i] + "` ("
        with open(tableNames[i] + ".csv", 'rU') as csvFile: 
            reader = csv.reader(csvFile)
            columns = next(reader)
            for i in range( len(columns)):
                columns[i] += ' varchar(30), '
            for column in columns:
                schemaFileText+= column
        ## at the end of each table we have to clip the ", " from the last element, requiring removing 2 characters. We also add proper statement end syntax.
        schemaFileText = schemaFileText[:-2] + ");\n"
    ## out of the loop: we're through each table and want to write back to the file.
    schemaFile.write(schemaFileText)
            
main()
