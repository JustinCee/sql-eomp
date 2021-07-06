from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry('500x500')
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

window.mainloop()
