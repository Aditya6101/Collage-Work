# importing required libraries
import mysql.connector

# Creating connection to MySQL 
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
password ="MySQL@123"
)

print("connected --> ", dataBase)

# preparing a cursor object
cursorObject = dataBase.cursor()

# using existing database -> python_test 
cursorObject.execute('USE python_test;')

# creating table query
# studentTable = """CREATE TABLE STUDENT (
#                    ROLL INT NOT NULL KEY,
#                    NAME  VARCHAR(20) NOT NULL,
#                    BRANCH VARCHAR(50),
#                    AGE INT
#                    );"""

# executing table query (studentTable)
# cursorObject.execute(studentTable)


# creating query to  insert data into table -> student
InsertIntoTable = "INSERT INTO student (ROLL, NAME, BRANCH, AGE) VALUES (%s, %s, %s, %s)"

# assining the data to be inserted into table -> student
# this can be an array also for inserting multiple values
valuesToBeInserted = ("001", "Jane Doe", "CS", "20")

# executing the query to insert data into table -> student
cursorObject.execute(InsertIntoTable, valuesToBeInserted)

# NOTE: mydb.commit() is required to make the changes to the table
dataBase.commit()

# disconnecting from server
dataBase.close()