from tkinter import *
from tkinter import messagebox as Messagebox


root = Tk()

def test():
	Messagebox.showinfo("Hello", "Hello World")
	
	Messagebox.showwarning("Warning", "Just Admins allowed")
	
	Messagebox.showerror("Error", "Critical Error")

	result = Messagebox.askquestion("Exit", "Are you sure?")
	if result == "yes":  # "no"
		root.destroy()

	result = Messagebox.askokcancel("Exit", "Override file?")
	if result:
		root.destroy()

	result = Messagebox.askyesno("Exit Boolean", "Are you sure?")
	if result:
		root.destroy()

	result = Messagebox.askretrycancel("Retry", "It can't connect")
	if result:
		root.destroy()


Button(root, text="Click me", command=test).pack()


root.mainloop()
