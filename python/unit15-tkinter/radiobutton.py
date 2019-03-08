from tkinter import *

root = Tk()

def select():
	monitor.config(text="{}".format(option.get()))

def reset():
	option.set(None)
	monitor.config(text="")

option = IntVar()

Radiobutton(root, text="option 1", variable=option, value=1, command=select).pack()
Radiobutton(root, text="option 2", variable=option, value=2, command=select).pack()
Radiobutton(root, text="option 3", variable=option, value=3, command=select).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="reset", command=reset).pack()

root.mainloop()
