from tkinter import ttk
import os
import tkinter as tk
import sqlite3
from tkinter import messagebox
from database import *

def logged(frame):
    allFrameItems = frame.winfo_children()
    for item in allFrameItems:
            item.destroy()
    print("Destroyed")


    setNickNameLabel = ttk.Label(frame, text="Nombre: ")
    setNickNameEntry = ttk.Entry(frame)
    setPasswordP1Label = ttk.Label(frame, text="Contraseña: ")
    setPasswordP1Label = ttk.Entry(frame)

    loginButtonP1 = ttk.Button(frame, text="Iniciar Sesion", command=lambda:login(nickNameP1Entry.get(), passwordP1Entry.get(), frameP1))

    nickNameP1Label.place(x=0, y=50)
    nickNameP1Entry.place(x=0, y=70)
    passwordP1Label.place(x=0, y=100)
    passwordP1Entry.place(x=0, y=120)

    loginButtonP1.place(x=250, y=300)

    testButton = ttk.Button(frame, text="hola")
    testButton.place(x=0, y=50)