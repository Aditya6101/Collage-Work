# importing required libraries
import mysql.connector

# Creating connection to MySQL 
dataBase = mysql.connector.connect(
host ="your_host",
user ="your_username",
password ="your_password"
)


print(dataBase)

mycursor = dataBase.cursor()

# Executing Query -> Creating Database
mycursor.execute("CREATE DATABASE python_test")

# Disconnecting from the server
dataBase.close()
