import Tkinter
from Tkinter import *
import tkMessageBox
from subprocess import call

top = Tkinter.Tk()
top.title("Cheat")
   
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
	
def rstprnt():
	E1F = E1.get()
	call("sc \\" + E1 + " stop spooler", shell=True)

	
complabel = Label(top, text="Computer name: ")
complabel.pack()
E1 = Entry(top, bd = 5)
E1.pack()	

B2 = Tkinter.Button(top, text ="Ping", width=20, command = ping)
# B3 = Tkinter.Button(top, text ="WDS", width=20, command = helloCallBack)
B4 = Tkinter.Button(top, text ="Tasklist", width=20, command = tasklist)
B5 = Tkinter.Button(top, text ="SN", width=20, command = sn)
B6 = Tkinter.Button(top, text ="Reset Spool", width=20, command = rstprnt)

B2.pack()
# B3.pack()
B4.pack()
B5.pack()
B6.pack()
top.mainloop()