from tkinter import *
from tkinter import messagebox
import mysql.connector

window = Tk()
window.title("Login Screen")
window.config(bg='yellow')
window.geometry('400x300')


def registering():
    if user_name_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Entry Error', 'Please enter your details')
    else:
        try:
            hospital = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                               database='Hospital',
                                               auth_plugin='mysql_native_password')
            mycursor = hospital.cursor()
            data = 'INSERT INTO Logins (user, password) VALUES (%s, %s)'
            value = (user_name_entry.get(), password_entry.get())
            mycursor.execute(data, value)
            hospital.commit()
            messagebox.showinfo("Good Day", 'You have been registered and you can now Login')
        except ValueError:
            messagebox.showinfo('Details invalid', 'Please make sure that the details you have entered match')
            user_name_entry.delete(0, END)
            password_entry.delete(0, END)


def logging_in():
    if user_name_entry == '':
        messagebox.showinfo("Error", 'Please enter your username')
    if password_entry == '':
        messagebox.showinfo('Error', 'Please enter your password')
    else:
        hospital = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                           database='Hospital',
                                           auth_plugin='mysql_native_password')
        mycursor = hospital.cursor()
        xy = mycursor.execute('SELECT * FROM Logins')
        for i in mycursor:
            if user_name_entry.get() == i[0] and password_entry.get() == i[1]:
                messagebox.showinfo('Access Granted', 'welcome to hospital')
                window.destroy()
                import next_screen

            elif user_name_entry.get() != i[0] and password_entry.get() != i[0]:
                messagebox.showinfo('Login Error', 'Please type in the correct details')


user_name = Label(window, text='Please enter your username', bg='yellow')
user_name.place(x=5, y=30)
user_name_entry = Entry(window)
user_name_entry.place(x=220, y=30)

password_label = Label(window, text='Please enter your password', bg='yellow')
password_label.place(x=5, y=100)
password_entry = Entry(window, show='*')
password_entry.place(x=220, y=100)

login_btn = Button(window, text='Login', fg='green', command=logging_in)
login_btn.place(x=100, y=200)

register_btn = Button(window, text='Register new user', command=registering)
register_btn.place(x=200, y=200)


def exiting():
    window.destroy()


exit_btn = Button(window, text='exit', fg='red', command=exiting)
exit_btn.place(x=340, y=260)

window.mainloop()
