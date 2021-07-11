from datetime import datetime, timedelta, date
from tkinter import *
import mysql.connector

window = Tk()
window.title('Sign In')
window.geometry('500x300')
window.config(bg='yellow')

main_label = Label(window, bg='yellow', font='Helvetica 13 underline',
                   text='Welcome to the Sign In screen. \n\nUpon entering the building CLICK the Sing In button. \n\nUpon leaving the building CLICK the Sign Out button')
main_label.place(x=40, y=10)

get_date = datetime.now().date().strftime("%Y-%m-%d")
get_time = datetime.now().time().strftime('%H:%M:%S')
identity = ""


def sign_in():
    signdb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                     database='LifechoicesDB',
                                     auth_plugin='mysql_native_password')
    mycursor = signdb.cursor()
    first = "INSERT INTO sign_in(id_number, sign_in, sign_in_date) VALUES (%s, %s, %s)"
    data_one = (get_time, get_date)
    mycursor.executemany(first, data_one)
    signdb.commit()


sign_in_btn = Button(window, width='30', text='Sign In', fg='green', command=sign_in)
sign_in_btn.place(x=120, y=150)

sign_out_btn = Button(window, width='30', text='Sign Out', fg='Blue')
sign_out_btn.place(x=120, y=200)


def exiting():
    window.destroy()


exit_btn = Button(window, text='exit', fg='red', command=exiting)
exit_btn.place(x=430, y=260)

window.mainloop()
