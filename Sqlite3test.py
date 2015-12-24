# Bradley Taniguchi
# test database handler with sqlite3 
# Python interaction example
# https://docs.python.org/2/library/sqlite3.html
# Sqlite3 example
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

# NOTE on Primary Keys, IE only 1 version. In full version it will be StudentID
# http://www.techonthenet.com/sqlite/primary_keys.php
# In this test we are just using Student names, which wouldn't function correctly as
#   students may have the same name, and thus ruin the programs ability to rent the room

import sqlite3
import os

databasefile = os.path.join(os.path.dirname(__file__), 'bin/TestDataBase.sqlite')  # for ./my_file
conn = sqlite3.connect(databasefile)  # connect to database
c = conn.cursor()

student_table1 = 'sq_student_table_1'  # name of table to be created
student_name_field = 'sq_student_col'  # name of column, organized by student name FOR NOW
student_name_field_type = 'TEXT'  # column data type, TEXT, or text string
student_id_field = 'sq_student_col'
student_id_field_type = 'INTEGER'

# NOTE: SQLITE has 5 datatypes:
#   NULL - returns the value NULL value
#   INTEGER - The value is a signed integer, stored in 1-8 bytes depending on magnitude
#   REAL - The value is floating point value, stored as an 8-byte IEEE floating point num
#   TEXT - The value is a text string, stored using the database encoding (UTF-8, UTF-16BE, UTF-16LE)
#   BLOB - The value is a blob of data, stored exactly as it was input

print("Starting Program...")
# creating a NEW SQLite table with 1 column
c.execute('CREATE TABLE {st}({sn} {snt})'.format(st=student_table1, sn=student_name_field, snt=student_name_field_type))

conn.commit()
conn.close()
def insertvalues(name, value):
    print("Using insertvalue function")
    try:
        c.execute("INSERT INTO {st} ({stname} {val})")
"""
#MUST use: conn.close() to close connection
# IF perform changes to database MUST use:
#   conn.commit()
#   conn.close()
"""