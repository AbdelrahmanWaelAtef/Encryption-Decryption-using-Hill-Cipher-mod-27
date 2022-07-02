import tkinter as tk
from tkinter import *
from Functions import *
from tkinter import ttk
import tkinter.font as font


def button1():
    key = keybox.get('1.0', END)
    key = key.strip()
    if len(key) != 9:
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text2)
        infobox.configure(state='disabled')
    elif checknum(key):
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text2)
        infobox.configure(state='disabled')
    elif not det_check(keygen(key)):
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text3)
        infobox.configure(state='disabled')
    else:
        message = mainbox.get()
        message = alpha_num(message)
        key = keygen(key)
        encrypted_msg = encrypt(message, key)
        encrypted_msg = num_alpha(encrypted_msg)
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, encrypted_msg)
        infobox.configure(state='disabled')


def button2():
    key = keybox.get('1.0', END)
    key = key.strip()
    if len(key) != 9:
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text2)
        infobox.configure(state='disabled')
    elif checknum(key):
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text2)
        infobox.configure(state='disabled')
    elif not det_check(keygen(key)):
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, text3)
        infobox.configure(state='disabled')
    else:
        message = mainbox.get()
        message = alpha_num(message)
        key = keygen(key)
        decrpted_msg = decyrption(message, key)
        decrpted_msg = num_alpha(decrpted_msg)
        infobox.configure(state='normal')
        infobox.delete('1.0', END)
        infobox.insert(END, decrpted_msg)
        infobox.configure(state='disabled')


r = tk.Tk()
r.iconbitmap('1.ico')
r.title("Hill Cipher (MOD 27)")
r.geometry("526x330")
r.resizable(width=FALSE, height= FALSE)
r.columnconfigure(0, weight=5)
r.columnconfigure(1, weight=5)

myfont = font.Font(family='Berlin Sans FB',size=11)

mainbox = Entry(r, width=85, bd=5)
mainbox.insert(0, 'Your message')
mainbox.grid(row=0, column=0, columnspan=2,  sticky="W", padx=5, pady=5)

text1 = 'How to use our program: \n1- Input your text in the      input entry box. \n2- Input your key in the key   entry box. \n3- Choose to either encrypt    or decrypt your text \n \nKey length must be 9          non-numerical charachters'
text2 = 'Key length must be 9          non-numerical charachters'
text3 = 'Invalid key'

infobox = Text(r, width=30, bd=5, height=10)
infobox.insert(END, text1)
infobox.configure(state='disabled')
infobox.grid(row=1, column=0, rowspan=2, sticky="W", padx=5, pady=5)

keybox = Text(r, height=5, width=30, bd=5, pady=5)
keybox.insert('1.0', 'Your key')
keybox.grid(row=1, column=1, sticky='w')

but1 = Button(r, text="Encrypt", width=35, height=5, bd=5, fg='Black', font=myfont, command=button1)
but1.grid(row=3, column=0, padx=5, pady=5)

but2 = Button(r, text="Decrypt", width=35, height=5, bd=5, fg='Black', font=myfont, command=button2)
but2.grid(row=3, column=1, padx=5, pady=5)


r.mainloop()

