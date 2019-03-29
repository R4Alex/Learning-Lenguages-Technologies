from tkinter import *

# root Configuration
root = Tk()

image = PhotoImage(file="giphy.gif")
Label(root, image=image, bd=0).pack()


root.mainloop()
