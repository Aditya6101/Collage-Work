import mysql.connector
import tkinter

root = tkinter.Tk()
root.geometry("300x300")

label = tkinter.Label(root,text="This is label")
label.pack()

lb = tkinter.Spinbox(root,text="kdfgaskg")
lb.pack()


		

redColorBtn = tkinter.Button(root, text='Red', width=25, command=changeLabelColor)

redColorBtn.pack()


def changeLabelColor(color):
	if(color == "red"):


root.mainloop()

