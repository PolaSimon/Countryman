import pymysql
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

sql_scripts = ["Country_code_table.sql", "countries.sql"]

for script in sql_scripts:

    with open(script, 'r') as sql_file:
        sql_script = sql_file.read()
        print(sql_script)

        cur = mydb.cursor()
        cur.execute("USE DB")
        try:
            cur.execute(sql_script)
        except Exception as e:
            print(e)
