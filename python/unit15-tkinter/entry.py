from  tkinter import *

root = Tk()

label = Label(root, text="Name")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="disable")

label2 = Label(root, text="Last Name")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center")


label3 = Label(root, text="password")
label3.grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry3 = Entry(root)
entry3.grid(row=1, column=1, padx=5, pady=5)
entry3.config(justify="center" show="*")



root.mainloop()