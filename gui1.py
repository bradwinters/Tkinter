#Import tkinter library
from tkinter import *

#Create an instance of Tkinter frame or window
# then Set the geometry of tkinter frame
win= Tk()
win.geometry("850x350")


def callback():
   Label(win, text="Hello universe 2", font=('Century 20 bold')).pack(pady=4)

#Create a Label and a Button widget
btn=Button(win, text="Press Enter", command= callback)
btn.pack(ipadx=10)
win.bind('<Return>',lambda event:callback())
win.mainloop()
