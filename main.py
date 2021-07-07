def logging_in():
    if id_entry == '':
        messagebox.showinfo("Error", 'Please enter your username')
    if password_entry == '':
        messagebox.showinfo('Error', 'Please enter your password')
    else:
        lifechoicesdb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                database='LifechoicesDB',
                                                auth_plugin='mysql_native_password')
        mycursor = lifechoicesdb.cursor()
        xy = mycursor.execute('SELECT * FROM Users')
        for i in mycursor:
            if id_entry.get() == i[0] and password_entry.get() == i[1]:
                messagebox.showinfo('Access Granted', 'Welcome to LifeChoices')

            elif id_entry.get() != i[0] and password_entry.get() != i[0]:
                messagebox.showinfo('Login Error', 'Please type in the correct details')
