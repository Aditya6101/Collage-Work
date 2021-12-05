# importing required libraries
import mysql.connector

# Creating connection to MySQL 
dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
password ="MySQL@123"
)


print(dataBase)

mycursor = dataBase.cursor()

# Executing Query -> Creating Database
mycursor.execute("CREATE DATABASE python_test")

# Disconnecting from the server
dataBase.close()
