from tkinter import *


def sum():
	r.set(float(n1.get()) + float(n2.get()))

def subtraction():
	r.set(float(n1.get()) + float(n2.get()))

def multiplication():
	r.set(float(n1.get()) + float(n2.get()))

root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Num 1").pack()
Entry(root, justify="center", textvariable=n1).pack()

Label(root, text="Num 2").pack()
Entry(root, justify="center", textvariable=n2).pack()

Label(root, text="\nResult").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()

Label(root, text="").pack()


Button(root, text="Sum", command=sum).pack(side="left")
Button(root, text="Subtraction", command=subtraction).pack(side="left")
Button(root, text="Multiplication", command=multiplication).pack(side="left")


root.mainloop()
