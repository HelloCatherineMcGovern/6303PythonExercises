from pathlib import Path
import csv
import json
import sqlite3

"""
Here is the assignment prompt
Pretend your company has purchased a smaller rival 
company and you are tasked with programmatically inserting new 
customers into the chinook.db database. You are provided with a 
customers.csv file of 91 customers. Import those records into the 
chinool.db’s customer table using python. First, read the csv file 
and convert it to a list or tuple. Second, write the list or tuple 
to the chinook.db’s customer table. 
Both the customers.csv file and chinook.db file are in your repository. 
"""

print("read each row from a csv file")
with open("customers.csv") as file:
    reader = csv.reader(file)
#    for row in reader:
 #       print(row)
    customer_list = list(reader)
#   for customer in customer_list:
#      print(customer)
# INSERT INTO customers (FirstName, LastName, Company, Address, City, Country, PostalCode, Email) VALUES ("Alfreds Futterkiste","Maria","Anders","Obere Str. 57","Berlin",12209,"Germany","Maria.Anders@gmail.com")
# INSERT INTO customers (FirstName, LastName, Company, Address, City, Country, PostalCode, Email) VALUES (?,?,?,?,?,?,?,?)
db_name = "chinook-taskd.db"
with sqlite3.connect(db_name) as conn:
    sql_command = "INSERT INTO customers (Company, FirstName, LastName, Address, City, Country, PostalCode, Email) VALUES (?,?,?,?,?,?,?,?)"
 #   cursor = conn.execute(sql_command)
#    temp = cursor.fetchall()
#    print(temp)
    for customer in customer_list:
        customer_values = customer
        conn.execute(sql_command, customer_values)
conn.commit()
print("Data Written to the database")
