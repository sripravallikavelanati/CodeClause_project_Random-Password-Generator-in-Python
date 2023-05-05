import random
import string
import tkinter as tk
from tkinter import * 

def password_generate():
    password=''
    length=12
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    res.set(password)

calculator = tk.Tk()
calculator.title("Password Generator")
calculator.geometry("600x600")


Label(calculator,text = "Generate the Random Password",font=30,fg="blue").pack(pady=8)

res=StringVar()
submit = Button(calculator,text = "Click here to get password",font=20,width = 30,command = password_generate,fg="green").pack(pady=5)
Entry(calculator,text="password: ",textvariable=res,width=20,font=60,fg="red").pack()
calculator.mainloop()