from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry('500x500')
window.title('Welcome to LifeChoices')
window.config(bg='yellow')

canvas = Canvas(window, width=500, height=300, bg="Yellow", borderwidth=0, highlightthickness=0)
canvas.place(x=90, y=5)
img = ImageTk.PhotoImage(Image.open('Lifechoices-300x91.jpg'))
canvas.create_image(20, 20, anchor=NW, image=img)

main_label = Label(window,
                   text="If this is your first time then please Click the Register button \nif not then continue to Login",
                   bg='yellow', font='Helvetica 13 underline')
main_label.place(x=10, y=150)

name_label = Label(window, text="Please enter your name:", bg='yellow')
name_label.place(x=30, y=220)
name_entry = Entry(window)
name_entry.place(x=300, y=220)
window.mainloop()
