import mysql.connector
from datetime import datetime 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)
cur = mydb.cursor()
cur.execute("USE DB")

# item = "qwertyuio"
# order_time = "1998-04-18 16:48:36.76"
# date_obj = datetime.strptime(order_time, '%Y-%m-%d %H:%M:%S.%f')
# sql_stmt = f"INSERT INTO Orders(OrderTime, Item) VALUES('{date_obj}', '{item}')"
# cur.execute(sql_stmt)


sql_stmt = f"SELECT * FROM Countries"
cur.execute(sql_stmt)
response = cur.fetchall()
print(response)