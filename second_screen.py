import tkinter
from tkinter import *
from tkinter import messagebox

import mysql.connector
from PIL import ImageTk, Image

window = Tk()
window.geometry('500x650')
window.title('Register')
window.config(bg='yellow')

canvas = Canvas(window, width=500, height=300, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=60, y=5)
img = ImageTk.PhotoImage(Image.open('download (1).jpeg'))
canvas.create_image(20, 20, anchor=NW, image=img)

main_label = Label(window, text='Please enter the requested details below.', font='Helvetica 13 underline', bg='yellow')
main_label.place(x=85, y=180)

id_number = Label(window, text='ID Number:', bg='yellow')
id_number.place(x=10, y=220)
id_number_entry = Entry(window)
id_number_entry.place(x=300, y=220)
name_label = Label(window, text='Name:', bg='yellow')
name_label.place(x=10, y=260)
name_entry = Entry(window)
name_entry.place(x=300, y=260)
surname_label = Label(window, text='Surname:', bg='yellow')
surname_label.place(x=10, y=300)
surname_entry = Entry(window)
surname_entry.place(x=300, y=300)
cell_label = Label(window, text='Cellphone Number:', bg='yellow')
cell_label.place(x=10, y=340)
cell_entry = Entry(window)
cell_entry.place(x=300, y=340)
email_label = Label(window, text='E-Mail Address:', bg='yellow')
email_label.place(x=10, y=380)
email_entry = Entry(window, width=30)
email_entry.place(x=220, y=380)
password_label = Label(window, text='Please generate a Password:', bg='yellow')
password_label.place(x=10, y=460)
password_entry = Entry(window)
password_entry.place(x=300, y=460)

options_list = ['Student', 'Admin', 'Lecturer', 'Staff', "Visitor"]
value_inside = tkinter.StringVar(window)
value_inside.set("Select your Occupation")
role_menu = tkinter.OptionMenu(window, value_inside, *options_list)
role_menu.pack()
role_menu.place(x=270, y=420)
role_option = Label(window, text='Please select your Occupation:', bg='yellow')
role_option.place(x=10, y=420)


def registering():
    if name_entry.get() == '' or password_entry.get() == '' or id_number_entry.get() == '' or surname_entry.get() == '':
        messagebox.showerror('Entry Error', 'Please enter your details')
    else:
        try:
            lifechoicesdb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                    database='LifechoicesDB',
                                                    auth_plugin='mysql_native_password')
            mycursor = lifechoicesdb.cursor()
            data = 'INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s, %s,)'
            value = (id_number_entry.get(), name_entry.get(), surname_entry.get(), cell_entry.get(), email_entry.get(), value_inside.get(), password_entry.get())
            mycursor.execute(data, value)
            lifechoicesdb.commit()
            messagebox.showinfo("Good Day", 'You have been registered and you can now Login')
        except ValueError:
            messagebox.showinfo('Details invalid', 'Please make sure that the details you have entered match')
            name_entry.delete(0, END)
            password_entry.delete(0, END)


register_btn = Button(window, text='Register', fg='blue', command=registering)
register_btn.place(x=385, y=520)


def clear_fields():
    id_number_entry.delete(0, END)
    name_entry.delete(0, END)
    surname_entry.delete(0, END)
    cell_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


clear_btn = Button(window, text='Clear', command=clear_fields)
clear_btn.place(x=280, y=520)


def login_screen():
    window.destroy()
    import first_screen


login_btn = Button(window, text='Back to Login screen', fg='green', command=login_screen)
login_btn.place(x=10, y=520)

window.mainloop()
