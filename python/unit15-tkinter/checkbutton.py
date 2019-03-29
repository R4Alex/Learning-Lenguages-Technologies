from tkinter import *

def select():
	string = ""
	if(milk.get()):
		string += "milk "
	else:
		string += "no milk "


	if(sugar.get()):
		string += "sugar"
	else:
		string += "no sugar"

	monitor.config(text=string)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)


milk = IntVar()
sugar = IntVar()


image = PhotoImage(file="image.gif")
Label(root, image=image).pack(side="left")

frame = Frame(root)
frame.pack(side="right")


Label(frame, text="Ho do you want the coffee?").pack(anchor="w")
Checkbutton(frame, text="Milk:", variable=milk, onvalue=1, offvalue=0, command=select).pack(anchor="w")
Checkbutton(frame, text="Sugar:", variable=sugar, onvalue=1, offvalue=0, command=select).pack(anchor="w")


monitor = Label(frame)
monitor.pack()
frame.pack()

root.mainloop()