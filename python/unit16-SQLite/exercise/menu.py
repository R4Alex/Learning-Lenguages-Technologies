import sqlite3
from tkinter import *


def show_menu(frame):
    connection = sqlite3.connect("restaurant.db")
    cursor = connection.cursor()

    cursor.execute("select * from category")

    categories = cursor.fetchall()

    for category in categories:
        category_label = Label(frame, text=category[1])
        category_label.config(fg="blue", font=("Verdana", 26, 'bold'))
        category_label.pack()

        plates = cursor.execute("select name from plate where category_id='{}'".format(category[0]))

        for plate in plates:
            plate_label = Label(frame, text=plate[0])
            plate_label.config(fg="black", font=("Verdana", 20))
            plate_label.pack()

        Label(frame, text="\n").pack()

    connection.close()


root = Tk()
root.title("El Macho Mexican Restaurant")

frame = Frame(root, width=640, height=720)

frame.pack()

root.config(cursor="arrow")
root.config(bg="grey")
root.config(bd=25)
root.config(relief="ridge")

l1 = Label(frame, text=" !El Macho Mexican Restaurant! ")
l1.config(fg="green", font=("Verdana", 38, 'bold'))
l1.pack()


l2 = Label(frame, text="Day Menu\n")
l2.config(fg="green", font=("Verdana", 32))
l2.pack()

show_menu(frame)

root.mainloop()
