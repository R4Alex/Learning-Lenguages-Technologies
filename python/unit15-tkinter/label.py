from tkinter import *

# root Configuration
root = Tk()



text = StringVar()
text.set("A new text")

#frame = Frame(root, width=480, height=320)
#frame.pack()

#label = Label(root, text="Hello world!")
#label.pack()
#label.place(x=0, y=0)

Label(root, text="Hello world!").pack(anchor="nw")
label = Label(root, text="label!")
label.pack(anchor="center")
Label(root, text="last label!").pack(anchor="se")

label.config(bg="green", fg="blue", font=("verdana",24))
label.config(textvariable=text)

root.mainloop()
