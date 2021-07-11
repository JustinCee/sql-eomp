# below is all the modules i needed to import
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector

from PIL import ImageTk, Image
# below is the configuration of the window
window = Tk()
window.geometry('500x500')
window.title('Welcome to LifeChoices')
window.config(bg='yellow')
# Below is the configuration of the image file
canvas = Canvas(window, width=500, height=300, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=90, y=5)
img = ImageTk.PhotoImage(Image.open('Lifechoices-300x91.jpg'))
canvas.create_image(20, 20, anchor=NW, image=img)
# Below is all the labels and entries needed for my tkinter window
main_label = Label(window,
                   text="If this is your first time then please Click the Register button \nif not then continue to Login",
                   bg='yellow', font='Helvetica 13 underline')
main_label.place(x=10, y=150)

name_label = Label(window, text="Please enter your name:", bg='yellow')
name_label.place(x=30, y=220)
name_entry = Entry(window)
name_entry.place(x=300, y=220)

password_label = Label(window, text='Please enter your password', bg='yellow')
password_label.place(x=30, y=260)
password_entry = Entry(window, show='*')
password_entry.place(x=300, y=260)
# Below is an option list for the different users to login with
options_list = ['Student', 'Admin', 'Lecturer', 'Staff', "Visitor"]
value_inside = tkinter.StringVar(window)
value_inside.set("Select your Occupation")
role_menu = tkinter.OptionMenu(window, value_inside, *options_list)
role_menu.pack()
role_menu.place(x=272, y=300)
role_option = Label(window, text='Please select your Occupation:', bg='yellow')
role_option.place(x=30, y=300)


# Below is the function needed for the different users to login and it is added to the Login button
def logging_in():
    if name_entry == '':
        messagebox.showinfo("Error", 'Please enter your username')
    if password_entry == '':
        messagebox.showinfo('Error', 'Please enter your password')
    else:
        lifechoicesdb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                                database='LifechoicesDB',
                                                auth_plugin='mysql_native_password')
        mycursor = lifechoicesdb.cursor()
        xy = mycursor.execute('SELECT name, password, role FROM Users')
        for i in mycursor:
            if name_entry.get() == i[0] and password_entry.get() == i[1] and value_inside.get() != "":
                messagebox.showinfo('Access Granted', 'Welcome to LifeChoices')
                window.destroy()
                import new

            elif name_entry.get() == i[0] and password_entry.get() == i[1] and value_inside.get() == "Admin":
                messagebox.showinfo('Access Granted', 'You have made it to the Admin Page')
                window.destroy()
                import main

        if name_entry.get() != [0] and password_entry.get() != [0]:
            messagebox.showinfo('Login Error', 'Please type in the correct details')


# Below is the login button
login_btn = Button(window, text='Login', fg='green', command=logging_in)
login_btn.place(x=350, y=400)


# Below is the clear button and the register button and the exit button and in between is all their functions
def clearing():
    name_entry.delete(0, END)
    password_entry.delete(0, END)


clear_btn = Button(window, text='Clear', command=clearing)
clear_btn.place(x=200, y=400)


def register_screen():
    window.destroy()
    import second_screen


register_btn = Button(window, text='Register', fg='blue', command=register_screen)
register_btn.place(x=50, y=400)


def exiting():
    window.destroy()


exit_btn = Button(window, text='exit', fg='red', command=exiting)
exit_btn.place(x=440, y=462)

window.mainloop()
