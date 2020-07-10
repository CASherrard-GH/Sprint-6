import matplotlib.pyplot as plt

import pymysql
import mysql.connector
import xlrd 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="testdb"
    )
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE groceries")
#mycursor.execute("SHOW DATABASES")

#for db in mycursor:
#    print(db)

sqlFormula = "INSERT INTO groceries (Chips, Cooldrinks, Chocolates, Pies, Fruit, Cupcakes, Veggies) VALUES (%s, %s, %s, %s, %s, %s, %s)"
groceries = [("Simba", "Coke", "Cadbury", "Pepper Steak", "Pear", "Vanilla", "Orange"),
             ("Lays", "Fanta", "Tex", "Chicken", "Apple", "Chocolate", "Cabbage"),
             ("", "", "", "", "Orange", "", "")]
mycursor.executemany(sqlFormula, groceries)

mydb.commit()

amount = [2,2,2,2,3,2,2]
category = ["Chips", "Cooldrinks", "Chocolates", "Pies", "Fruit", "Cupcakes", "Veggies"]

plt.pie(amount, labels=category)
