import mysql.connector

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'binaryoptions',
  'raise_on_warnings': True,
  'use_pure': False,
}

cnx = mysql.connector.connect(**config)

cnx.close()