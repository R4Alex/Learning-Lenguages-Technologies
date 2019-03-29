from tkinter import *
from io import open
from tkinter import filedialog as FileDialog

route = "" 

def new():
	info.set("New File")
	global route
	route = ""
	text.delete(1.0, "end")
	root.title("My Editor")


def file_open():
	global route
	info.set("Open a File")
	route = FileDialog.askopenfilename(
		initialdir=".", 
		filetype=(
			("Text File", "*.txt"),
			("All Files", "*.*")
		),
		title="Open a Text File")
	
	if route != "":
		file = open(route, 'r')
		content = file.read()
		text.delete(1.0, "end")
		text.insert('insert', content)
		file.close
		root.title(route + " - My Editor")


def save():
	if route != "":
		content = text.get(1.0, 'end-1c')
		file = open(route, 'w+')
		file.write(content)
		file.close()
		info.set("File saved")
	else:
		save_as()

def save_as():
	global route

	file = FileDialog.asksaveasfile(title="Save File as", mode="w", defaultextension=".txt")

	if file is not None:
		route = file.name
		content = text.get(1.0, 'end-1c')
		file = open(route, 'w+')
		file.write(content)
		file.close()
		info.set("File saved")
	else:
		info.set("Save Canceled")
		route = ""

root = Tk()
root.title("Mi editor")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=file_open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save as...", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="File")


# Main Text Editor
text = Text(root)
text.pack(fill="both", expand=1)
text.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# info monitor label
info = StringVar()
info.set("Welcome to your Editor")

monitor = Label(root, textvar=info)
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()