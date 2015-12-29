#!/usr/bin/env python3
# Bradley Taniguchi
# 12/21/15

from datetime import datetime
import os
import sqlite3


class Student:
    """
    Handles student objects populates StudentCollection
    """
    def __init__(self, studentid=0, name="John Doe"):
        self.name = name  # if not given an input, use default IE John Doe
        self.studentid = studentid


class StudentCollection:
    """
    Student handler and creation aspect.
    """
    def __init__(self, listofstudents=None):  # DO NOT USE: list = [], GOTME!
        if listofstudents is None:
            listofstudents = []  # list of student classes
    # WORK HERE WITH SEARCH ALGORITHM IF NEEDED!


class DataBaseInterface:
    """
    Primary Database interface handler
    """
    def __init__(self, filename='bin/Sqlite/StudentDatabase.sqlite'):
        self.filedirectory = filename
        self.databasefile = os.path.join(os.path.dirname(__file__), filename)
        #self.conn = sqlite3.connect(self.databasefile) # forgot about conn.commit, conn.close
        #self.c = self.conn.cursor()
        if os.path.isfile(filename):
            print(">DEBUG: File Exists!")

    def _createstudentdatabase(self):
        """
        Creates The Student Database if there isn't one already
        :return: true if creating database was a succuess
        """
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        print(">DEBUG: Creating Student Database at: " + self.filedirectory)
        c.execute('''CREATE TABLE student_table1
                 (ID INT PRIMARY KEY NOT NULL,
                  NAME CHAR(32) NOT NULL,
                  CLOCKIN TEXT NOT NULL,
                  CLOCKOUT TEXT)''')
        conn.commit()
        conn.close()

    def clockin(self, studentidnumber, studentname):  # clock into a room
        """
        Creates a Student Entry into the database.
        :param studentidnumber: ID number of student, PRIMARY KEY for searches
        :param studentname: Name of Student logging in.
        """
        conn = sqlite3.connect(self.databasefile)  # create connection to database
        c = conn.cursor()
        clockintime = str(datetime.now().time().hour) + ":" + str(datetime.now().time().minute)  # doesn't include secs
        mytuple = [studentidnumber, studentname, clockintime]
        print(">DEBUG: Using insertvalue function")
        try:
            c.execute("INSERT INTO {0} ({1}, {2}, {3}, {4})".format(
                    self.databasefile, mytuple[0], mytuple[1], mytuple[2]))
            print("SUCCESS: Added Student login:" + studentname + " at " + clockintime)  # make this return statement!
        except sqlite3.IntegrityError:
            print("ERROR: Sqlite3 Integrity Error")  # make this return statement!
        conn.commit()
        conn.close()

    @staticmethod
    def clockout(studentidnumber, studentname):  # clock out of a room
        """
        :param studentidnumber: Primary Key for Searches
        :param studentname:  Seconary key for Searches, If unmatched raise exception
        :return:
        """
        print(">DEBUG: Clockout function attempted...")