from tkinter import *

# root Configuration
root = Tk()

frame = Frame(root, width=480, height=320)
frame.pack()

label = Label(frame, text="Hello world!")
#label.pack()
label.place(x=0, y=0)

"""
# Dynamic text Variables
text = StringVar()
text.set("New Text")

Label(root, text="Hello world").pack(anchor="nw")

lab = Label(root, text="Label")
lab.pack(anchor="center")
lab.config(bg="green", fg="blue", font=("Verdana", 24))

Label(root, text="Another Label").pack(anchor="se")



image = PhotoImage(file="giphy.gif")
Label(root, image=image, bd=0).pack(side="left")
"""


root.mainloop()
