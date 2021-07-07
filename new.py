from tkinter import *

window = Tk()
window.title('Sign In')
window.geometry('500x500')
window.config(bg='yellow')

main_label = Label(window, bg='yellow', font='Helvetica 13 underline', text='Welcome to the Sign In screen. \n\nUpon entering the building CLICK the Sing In button. \n\nUpon leaving the building CLICK the Sign Out button')
main_label.place(x=40, y=10)

window.mainloop()
