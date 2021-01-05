from tkinter import *
from time import strftime
root=Tk()
def time():
	clock=strftime("%I:%M:%S %p")   #if you want 24 Hour clock just type %H in %I position...(%I=12 hour)& (%H=24 hour)
	label.configure(text=clock)
	label.after(1000,time)
label=Label(root,fg="green",bg="Black",height=40,width=80)
label.pack()
time()
root.mainloop()
