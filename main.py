# below is al the modules that i needed to import
import tkinter
from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector

# below is the configuration of the window
admin = Tk()
admin.title("Admin Account")
admin.geometry('1000x700')
admin.config(bg='yellow')
# below is linking mysql to python
lifechoicesdb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234', host='127.0.0.1',
                                        database='LifechoicesDB',
                                        auth_plugin='mysql_native_password')

connect = lifechoicesdb.cursor()
connect.execute("SELECT * FROM Users")
# this is the configuration of the tree view table
tree = ttk.Treeview(admin)
tree['show'] = 'headings'

s = ttk.Style(admin)
s.theme_use('clam')

tree["columns"] = ('id_number', 'name', 'surname', 'cellnumber', 'email', 'role', 'password')

tree.column('id_number', width=130, minwidth=50, anchor=tkinter.CENTER)
tree.column('name', width=100, minwidth=50, anchor=tkinter.CENTER)
tree.column('surname', width=100, minwidth=50, anchor=tkinter.CENTER)
tree.column('cellnumber', width=150, minwidth=50, anchor=tkinter.CENTER)
tree.column('email', width=300, minwidth=50, anchor=tkinter.CENTER)
tree.column('role', width=100, minwidth=50, anchor=tkinter.CENTER)
tree.column('password', width=100, minwidth=50, anchor=tkinter.CENTER)

tree.heading('id_number', text='ID Number', anchor=tkinter.CENTER)
tree.heading('name', text='Name', anchor=tkinter.CENTER)
tree.heading('surname', text='Surname', anchor=tkinter.CENTER)
tree.heading('cellnumber', text='Cellphone Number', anchor=tkinter.CENTER)
tree.heading('email', text='E-Mail Address', anchor=tkinter.CENTER)
tree.heading('role', text='Role', anchor=tkinter.CENTER)
tree.heading('password', text='Password', anchor=tkinter.CENTER)

i = 0
for ro in connect:
    tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
    i = i + 1

# vsb = ttk.Scrollbar(admin, orient='vertical')

# vsb.configure(command=tree.yview)
# tree.configure(yscrollcommand=vsb.set)
# vsb.pack(fill=Y, side=RIGHT)

tree.pack()
tree.place(x=10, y=100)

ID = StringVar()
name = StringVar()
surname = StringVar()
phone = IntVar()
email = StringVar()
role = StringVar()
password = StringVar()


# below is the function needed to add data to the tree view table and to my database
def add_data(tree):
    frame = Frame(admin, width=400, height=400, bg='grey')
    frame.place(x=100, y=150)
    label1 = Label(frame, text='ID:', width=10)
    entry1 = Entry(frame, textvariable=ID, width=20)
    label1.place(x=50, y=30)
    entry1.place(x=170, y=30)

    label2 = Label(frame, text='Name:', width=10)
    entry2 = Entry(frame, textvariable=name, width=20)
    label2.place(x=50, y=70)
    entry2.place(x=170, y=70)

    label3 = Label(frame, text='Surname:', width=10)
    entry3 = Entry(frame, textvariable=surname, width=20)
    label3.place(x=50, y=110)
    entry3.place(x=170, y=110)

    label4 = Label(frame, text='Cell Number', width=10)
    entry4 = Entry(frame, textvariable=phone, width=20)
    label4.place(x=50, y=150)
    entry4.place(x=170, y=150)
    entry4.delete(0, END)

    label5 = Label(frame, text='Email:', width=10)
    entry5 = Entry(frame, textvariable=email, width=20)
    label5.place(x=50, y=190)
    entry5.place(x=170, y=190)

    label6 = Label(frame, text='Role:', width=10)
    entry6 = Entry(frame, textvariable=role, width=20)
    label6.place(x=50, y=230)
    entry6.place(x=170, y=230)

    label7 = Label(frame, text='Password:', width=10)
    entry7 = Entry(frame, textvariable=password, width=20)
    label7.place(x=50, y=270)
    entry7.place(x=170, y=270)

    # below is to insert data into the table and my database
    def insert_data():
        nonlocal entry1, entry2, entry3, entry4, entry5, entry6, entry7
        num_id = ID.get()
        firstname = name.get()
        lastname = surname.get()
        num = phone.get()
        mail = email.get()
        occ = role.get()
        pword = password.get()
        connect.execute(
            'INSERT INTO Users(id_number, name, surname, cellnumber, email, role, password) VALUES(%s, %s, %s, %s, %s, %s, %s)',
            (num_id, firstname, lastname, num, mail, occ, pword))
        print(connect.lastrowid)
        lifechoicesdb.commit()
        tree.insert('', 'end', text="", values=(num_id, firstname, lastname, num, mail, occ, pword))
        messagebox.showinfo('Success', 'User Details Added')
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        frame.destroy()

    # below is to close the insert data frame
    def close():
        frame.destroy()

    submit_btn = Button(frame, text='Submit', command=insert_data, font=('Times', 11, 'bold'), bg='green', fg='white')
    submit_btn.place(x=100, y=320)
    cancel_btn = Button(frame, text='Cancel', font=('Times', 11, 'bold'), bg='red', fg='white', command=close)
    cancel_btn.place(x=240, y=320)


# below is the function needed to delete data from my database and from the treeview table
def delete_data(tree):
    select_items = tree.selection()[0]
    print(tree.item(select_items)['values'])
    pid = tree.item(select_items)['values'][0]
    del_data = "DELETE FROM Users WHERE id_number = %s"
    sel_data = (pid,)
    connect.execute(del_data, sel_data)
    lifechoicesdb.commit()
    tree.delete(select_items)
    messagebox.showinfo('Success', 'Data has been deleted')


# below are my insert and delete buttons
insert_btn = Button(admin, text='Insert', command=lambda: add_data(tree), font=('calibri', 14, 'bold'), bg='green',
                    fg='white')
insert_btn.place(x=300, y=350)

delete_btn = Button(admin, text='Delete', command=lambda: delete_data(tree), font=('calibri', 14, 'bold'), bg='red',
                    fg='white')
delete_btn.place(x=600, y=350)

main_label = Label(admin, text='Administrator', bg='yellow', font='Helvetica 25 underline')
main_label.place(x=400, y=5)


# below is the function to close the admin window and the exit button
def leaving():
    admin.destroy()


exit_btn = Button(admin, text='Exit', font=('calibri', 14, 'bold'), bg='white', fg='red', command=leaving)
exit_btn.place(x=900, y=450)

admin.mainloop()
