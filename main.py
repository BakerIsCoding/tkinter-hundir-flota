from tkinter import ttk
import os
import tkinter as tk
import sqlite3
from tkinter import messagebox
from login import login
from database import *
from loggedInterface import *
#Folder Name
dbOriginDir = "db"
#Database Name
dbName = "game.db"
#Full Database Path
fullDbPath = dbOriginDir + "/" + dbName
loggedUsers = ["", ""]



default = tk.Tk()
# Styles
style = ttk.Style()
style.configure('TButton', background='red')
style.configure('TButton', font=('roboto', 10), borderwidth='4')
style.configure('Label.TLabel', font=('Arial', 12))
style.map('TButton', foreground=[('active', '!disabled', 'Navy Blue')], background=[
          ('active', 'Navy Blue'), ('!disabled', 'black')], )

#Create Database
createDb()

default.geometry("1050x430")
default.resizable(False, False)
default.config(bg="blue")
default.config(relief="sunken")
default.config(bd=25)
# titleLabel = tk.Label(default, text="logeasion en la base de datos", font=("Arial", 14, "bold")).place(x=50, y=5)

# LEFT FRAME
frameP1 = tk.Frame(default, width=400, height=380)
frameP1.config(relief="sunken")
frameP1.config(bd=25)

frameP1.pack(side=tk.LEFT)
frameP1.config(bg="lightblue")

nickNameP1Label = ttk.Label(frameP1, text="Nombre: ")
nickNameP1Entry = ttk.Entry(frameP1)
passwordP1Label = ttk.Label(frameP1, text="Contraseña: ")
passwordP1Entry = ttk.Entry(frameP1)



nickNameP1Label.place(x=0, y=50)
nickNameP1Entry.place(x=0, y=70)
passwordP1Label.place(x=0, y=100)
passwordP1Entry.place(x=0, y=120)

# El command tiene la siguiente explicación, ejecuto la función "logged(frameP1)" 
# UNICAMENTE SI login(username, password, default, 1, loggedUsers) NO ES IGUAL A "loggedUsers[1]" 
# La variable loggedUsers contiene en la posicion 0 el nombre del jugador 1 y en la posición 1 el nombre del jugador 2
loginButtonP1 = ttk.Button(frameP1, text="Iniciar Sesion", command=lambda: (logged(frameP1) if not login(nickNameP1Entry.get(), passwordP1Entry.get(), default, 1, loggedUsers) == loggedUsers[1] else messagebox.showerror(title=None, message="No puedes jugar con el mismo usuario tt")))
loginButtonP1.place(x=250, y=300)


# MID FRAME
frameMid = tk.Frame(default, width=200, height=380)
frameMid.config(relief="groove")
frameMid.config(bd=25)

frameMid.pack(side=tk.LEFT)
frameMid.config(bg="gray")

# RIGHT FRAME
frameP2 = tk.Frame(default, width=400, height=380)
frameP2.config(relief="sunken")
frameP2.config(bd=25)

frameP2.pack(side=tk.LEFT)
frameP2.config(bg="tomato")

nickNameP2Label = ttk.Label(frameP2, text="Nombre: ")
nickNameP2Entry = ttk.Entry(frameP2)
passwordP2Label = ttk.Label(frameP2, text="Contraseña: ")
passwordP2Entry = ttk.Entry(frameP2)


nickNameP2Label.place(x=0, y=50)
nickNameP2Entry.place(x=0, y=70)
passwordP2Label.place(x=0, y=100)
passwordP2Entry.place(x=0, y=120)


# El command tiene la siguiente explicación, ejecuto la función "logged(frameP2)" 
# UNICAMENTE SI login(username, password, default, 2, loggedUsers) NO ES IGUAL A "loggedUsers[0]" 
# La variable loggedUsers contiene en la posicion 0 el nombre del jugador 1 y en la posición 1 el nombre del jugador 2
loginButtonP2 = loginButtonP2 = ttk.Button(frameP2, text="Iniciar Sesion", command=lambda: (logged(frameP2) if not login(nickNameP2Entry.get(), passwordP2Entry.get(), default, 2, loggedUsers) == loggedUsers[0] else messagebox.showerror(title=None, message="No puedes jugar con el mismo usuario tt")))
loginButtonP2.place(x=250, y=300)


resetButton = ttk.Button(frameMid, text="Crear usuario", command=createUser)
sendButton = ttk.Button(frameMid, text="Empezar partida", state= "disabled")
sendButton.place(x=25, y=100)
resetButton.place(x=32, y=150)

default.mainloop()
