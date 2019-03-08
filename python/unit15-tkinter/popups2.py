from tkinter import *
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog


root = Tk()

def test():
	color = ColorChooser.askcolor(title="Pick a color")
	print(color)

	route = FileDialog.askopenfilename(title="Open a file", initialdir="C:", 
		filetypes=(
				("Text files", "*.txt"),
				("Text files Advanced", ".txt2"),
				("All Files", "*.*"),
			)
	)
	
	# Like open('ruta', 'w') becarefull
	file = FileDialog.asksaveasfile(title="Save a File", mode="w", defaultextension=".txt") # mode="a" "r" "r+" "w"
	print(route)

	if file is not None:
		file.write("Hello")
		file.close()


Button(root, text="Click me", command=test).pack()


root.mainloop()
