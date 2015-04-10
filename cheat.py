import Tkinter
from Tkinter import *
import tkMessageBox
from subprocess import call

top = Tkinter.Tk()
top.title("Cheat")

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")
   
def ping():
	E1F = E1.get()
	call("ping " + E1F, shell=True)
	
"""
def wds()
	E1F = E1.get()
"""

def tasklist():
	E1F = E1.get()
	call("psexec \\" + E1F + " tasklist", shell=True) 
	
def sn():
	E1F = E1.get()
	call("wmic /node:" + E1F +" bios get serialnumber", shell=True)

	
complabel = Label(top, text="Computer name: ")
complabel.pack()
E1 = Entry(top, bd = 5)
E1.pack()	

B = Tkinter.Button(top, text ="Hello", width=20, command = helloCallBack)
B2 = Tkinter.Button(top, text ="Ping", width=20, command = ping)
B3 = Tkinter.Button(top, text ="WDS", width=20, command = helloCallBack)
B4 = Tkinter.Button(top, text ="Tasklist", width=20, command = tasklist)
B5 = Tkinter.Button(top, text ="SN", width=20, command = sn)
B6 = Tkinter.Button(top, text ="Reset Spool", width=20, command = helloCallBack)

B.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
B6.pack()
top.mainloop()