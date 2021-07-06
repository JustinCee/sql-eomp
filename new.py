import mysql.connector

LifechoicesDB = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                        database='LifechoicesDB',
                                        auth_plugin='mysql_native_password')

mycursor = LifechoicesDB.cursor()
xy = mycursor.execute('select * from Users')
for i in mycursor:
    print(i)
