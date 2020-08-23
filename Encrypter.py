from tkinter import *
import tkinter as tk 
from tkinter import messagebox
import base64
def lock():
    message = enter.get()
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    display_search(base64_message)
    messagebox.showinfo("ENCRYPTED","succesfully ENCRYPTED ")
    print(base64_message)


def unlock():
	base64_message = enter1.get()
	base64_bytes = base64_message.encode('ascii')
	message_bytes = base64.b64decode(base64_bytes)
	message = message_bytes.decode('ascii')
	display_search1(message)
	messagebox.showinfo("DECRYPTED","succesfully DECRYPTED ")
	print(message)

def display_search(base64_message):
    listbox= Listbox(frame,width=20,height=1)
    listbox.grid(row=7,column=0)
    listbox.insert(END,base64_message)
def display_search1(message):
    listbox= Listbox(frame,width=20,height=1)
    listbox.grid(row=8,column=0)
    listbox.insert(END,message)
root = Tk()
root.title("ENCRYPTER AND DECRYPTER")
canvas = Canvas(width=500,height=100)
canvas.pack()
frame = Frame()
frame.place(relx=0.05,rely=0.1,relwidth=0.9,relheight=0.8)
label=Label(frame,text="WORD TO ENCRYPT")
label.grid(row=1,column=1)
ENCRYPT=StringVar()
normal=StringVar()
enter=Entry(frame,textvariable="normal")
enter.grid(row=1,column=2)

btn=Button(frame,text="ENCRYPT",command=lambda:lock())
btn.grid(row=1,column=3)

label=Label(frame,text="WORD TO DECRYPT")
label.grid(row=2,column=1)
ENCRYPT=StringVar()
normal=StringVar()
enter1=Entry(frame,textvariable="normal1")
enter1.grid(row=2,column=2)

btn=Button(frame,text="DECRYPT",command=lambda:unlock())
btn.grid(row=2,column=3)
root.mainloop()