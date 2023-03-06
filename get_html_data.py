import pandas as pd
import mysql.connector
from unidecode import unidecode


connection = mysql.connector.connect(
    host='localhost', 
    user='root', 
    password='password')

cursor = connection.cursor()

df = pd.read_html('https://www.iban.com/country-codes')[0]
df['Numeric'] = df['Numeric'].astype(str).str.zfill(3)
list_of_rows = df.to_dict('records')

for entity in list_of_rows:
    try:
        country = entity.get('Country')
        alpha2 = entity.get('Alpha-2 code')
        alpha3 = entity.get('Alpha-3 code')
        numeric = entity.get('Numeric')
        cursor.execute("USE DB")
        sql_insert = f'''INSERT INTO Country_codes (Country_code, Alpha2_code, Alpha3_code, Numeric_code)
    VALUES ('{unidecode(country.replace("'","`"))}', '{alpha2}', '{alpha3}', '{numeric}')'''
        cursor.execute(sql_insert)
        connection.commit()
    except Exception as err:
        print(f"Unexpected {err} , {type(err)=}")

connection.close()