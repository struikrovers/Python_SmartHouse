import mysql.connector as connection

connectionstring = """user='demoticaproject', password='wuqExu37V1c11546z2BI3AfEWA78Be', host='demotica.marrokev.com', database='demoticaproject'"""

try:
  cnx = connection.connect(connectionstring)

except connection.Error as err:
  if err.errno == connection.errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == connection.errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()