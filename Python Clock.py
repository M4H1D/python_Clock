from tkinter import *
from time import strftime
root=Tk()
def time():
	clock=strftime("%H:%M:%S %p")
	label.configure(text=clock)
	label.after(1000,time)
label=Label(root,fg="green",bg="Black",height=40,width=80)
label.pack()
time()
root.mainloop()