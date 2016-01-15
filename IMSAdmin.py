#!/usr/bin/env python3
# Bradley Taniguchi
# 1/11/16

from datetime import datetime
import os
import sqlite3

import os
import sys
import sqlite3
from datetime import datetime
from SLC import Student
from SLC import StudentCollection

class IMSAdmin:
    def __init__(self, datfilepath="bin/Sqlite/StudentDatabase.sqlite", tablename="student_table1",
                 outputfile="bin/Printout.txt"):
        self.databasefilepath = os.path.join(os.path.dirname(__file__), str(datfilepath))
        self.databasetable = str(tablename)
        self.mystudentcollection = self.readdatabase()
        self.outputfilepath = os.path.join(os.path.dirname(__file__), str(outputfile))

    def prompt(self):
        print("Starting IMSAdmin....")
        while True:
            print("===MAIN PAGE===")
            print("[1] View Contents of Database")
            print("[2] Print Contents of Entire Database")
            print("[3] Modify database files]")
            print("[0] Exit")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                self.viewcontents()
            elif userinput == "2":
                self.clearscreen()
                self.printcontents()
            elif userinput == "3":
                self.clearscreen()
                self.modifycontents()
            elif userinput == "0":
                print("Program Exiting...")
                sys.exit(0)
            else:
                print("Bad Input")
                self.prompt()
            break

    def readdatabase(self):
        """
        Reads the Whole Database during startup of the program
        :return: Collection of entire database students
        """
        conn = sqlite3.connect(self.databasefilepath)
        c = conn.cursor()
        c.execute("SELECT * FROM " + self.databasetable)
        myrawlist = c.fetchall()
        conn.commit()
        conn.close()
        mystudentcollection = StudentCollection()
        mystudentcollection.convertraw(myrawlist)
        return mystudentcollection

    def viewcontents(self):  ##########################################################################################
        while True:
            print("===VIEW CONTENTS===")
            print("[1] View All Time Logins for table " + self.databasetable)
            print("[2] View Daily Logins for table " + self.databasetable)
            print("[3] View Logged In Students for Table" + self.databasetable)
            print("[0] GoBack")
            print("\n")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                self.view_alltime()
            elif userinput == "2":
                self.clearscreen()
                self.view_dailycontroller()
            elif userinput == "3":
                self.clearscreen()
                self.view_loggedin()
            elif userinput == "0":
                self.clearscreen()
                self.prompt()
            else:
                self.clearscreen()
                print("Bad Input")
                self.viewcontents()
            break  # gets here?

    def view_alltime(self):
        print("Datbase at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        for student in self.mystudentcollection.listofstudents:
            print(student.printvalues())

    def view_dailycontroller(self):
        while True:
            print("===Daily Entries===")
            print("[1] Todays Date")
            print("[2] Custom Date")
            print("[0] GoBack")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                self.view_daily(str(datetime.now().date()))  # TODAYS DATE!
                break
            elif userinput == "2":
                self.clearscreen()
                print("===Custom Date==")
                year = input("Year: ")
                if len(year) == 1:
                    year = "0" + year
                month = input("Month: ")
                if len(month) == 1:
                    month = "0" + month
                day = input("Day: ")
                if len(day) == 1:
                    day = "0" + day
                mydate = (str(year) + "-" + str(month) + "-" + str(day))
                self.view_daily(mydate)
                break
            elif userinput == "0":
                self.clearscreen()
                self.viewcontents()
            break

    def view_daily(self, datestring):  # EDI THIS
        print(str(datestring)) #2016-01-15
        print("Datbase at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        mystudentcollection = StudentCollection()
        for student in self.mystudentcollection.listofstudents:
            if student.clockindate == datestring:  # DEBUG THIS!
                mystudentcollection.listofstudents.append(student)
        for student in mystudentcollection.listofstudents:
            print(student.printvalues())

    def view_loggedin(self):
        print("Datbase at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        mystudentcollection = StudentCollection()
        for student in self.mystudentcollection.listofstudents:
            if student.clockouttime == "None":  # DEBUG THIS!
                mystudentcollection.listofstudents.append(student)
        for student in mystudentcollection.listofstudents:
            print(student.printvalues())

    def printcontents(self):  #########################################################################################
        while True:
            print("===PRINT CONTENTS===")
            print("[1] Print All Time Logs for " + self.databasetable)
            print("[2] Print Monthly Logs for " + self.databasetable)
            print("[3] Print Daily Logs for " + self.databasetable)
            print("[0] GoBack")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                self.print_alltime()
                break
            elif userinput == "2":
                self.clearscreen()
                print("NonFunctional!")
                #self.print_monthly()
            elif userinput == "3":
                self.clearscreen()
                self.print_dailycontroller()
                break
            elif userinput == "0":
                self.clearscreen()
                self.prompt()
                break
            else:
                self.clearscreen()
                print("Bad Input")
                self.printcontents()
            break

    def print_alltime(self):
        print("===PRINTING CONTENTS ALL TIME===")
        print("Datbase at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        print("Output file at: " + str(self.outputfilepath))
        myfile = open(str(self.outputfilepath), 'w')
        myfile.write("DATAOUTPUT DUMP " + str(datetime.now().date()) + "\n")
        for student in self.mystudentcollection.listofstudents:
            myfile.write(">" + student.printvalues()+"\n")
        print("Done!")

    def print_monthly(self):
        print("NON FUNCTIONAL US ALLTIME!")
        '''print("===PRINTING CONTENTS MONTHLY===")
        print("Database at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        print("Output file at: " + str(self.outputfilepath))
        myfile = open(str(self.outputfilepath), 'w')
        myfile.write("DATAOUTPUT DUMP " + str(datetime.now().date()) + "\n")
        mystudentcollection = StudentCollection()
        for student in self.mystudentcollection.listofstudents:
            mymonth = student.clockindate
            if mymonth == datetime.now().date().month:  # DEBUG THIS!
                mystudentcollection.listofstudents.append(student)
        for student in mystudentcollection.listofstudents:
            myfile.write((">" + student.printvalues() + "\n"))
        print("Done!")'''

    def print_dailycontroller(self):
        while True:
            print("===Daily Entries===")
            print("[1] Todays Date")
            print("[2] Custom Date")
            print("[0] GoBack")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                self.print_daily(str(datetime.now().date()))  # TODAYS DATE!
                break
            elif userinput == "2":
                self.clearscreen()
                print("===Custom Date==")
                year = input("Year: ")
                if len(year) == 1:
                    year = "0" + year
                month = input("Month: ")
                if len(month) == 1:
                    month = "0" + month
                day = input("Day: ")
                if len(day) == 1:
                    day = "0" + day
                mydate = (str(year) + "-" + str(month) + "-" + str(day))
                self.print_daily(mydate)
                break
            elif userinput == "0":
                self.clearscreen()
                self.printcontents()
            break

    def print_daily(self, datestring):
        print("===PRINTING CONTENTS DAILY===")
        print("Datbase at: " + str(self.databasefilepath) + " Table: " + str(self.databasetable))
        print("Output file at: " + str(self.outputfilepath))
        myfile = open(str(self.outputfilepath), 'w')
        myfile.write("DATAOUTPUT DUMP " + str(datetime.now().date()) + "\n")
        mystudentcollection = StudentCollection()
        for student in self.mystudentcollection.listofstudents:
            if student.clockindate == datestring:  # DEBUG THIS!
                mystudentcollection.listofstudents.append(student)
        for student in mystudentcollection.listofstudents:
            myfile.write((">" + student.printvalues() + "\n"))
        print("Done!")

    def modifycontents(self):  ########################################################################################
        while True:
            print("===MODIFY CONTENTS===")
            print("[1] Change Table Name")
            print("[2] Backup Database")
            print("[0] GoBack")
            userinput = input(">: ")
            if userinput == "1":
                self.clearscreen()
                print("NONFUNCTIONAL")
                #self.mod_changetablename()
                break
            elif userinput == "2":
                self.clearscreen()
                print("NONFUNCTIONAL")
                #self.mod_backupdatabase()
                break
            elif userinput == "0":
                self.clearscreen()
                self.prompt()
                break
            else:
                self.clearscreen()
                print("BadInput")
                self.modifycontents()
            break

    @staticmethod
    def clearscreen():
        print("\n\n\n\n\n")
        print("\n\n\n\n\n")


def main():
    myadmin = IMSAdmin()
    myadmin.prompt()

if __name__ == '__main__':
    main()