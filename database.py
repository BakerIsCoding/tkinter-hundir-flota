import os
import tkinter as tk
import sqlite3
from tkinter import messagebox
#Folder Name
dbOriginDir = "db"
#Database Name
dbName = "game.db"
#Full Database Path
fullDbPath = dbOriginDir + "/" + dbName


def selectNickname(nickname):
    #Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM players WHERE nickname=?", (nickname, ))

    results = cursor.fetchall()
    return results

def insertUser(nickEnt, passwdEnt):
    #Conexión a la base de datos.
    conectar = sqlite3.connect(fullDbPath)
    cursor = conectar.cursor()
    #Mientras no haya ningún campo vacío.
    if nickEnt.get() and passwdEnt.get():
        try:
            #Envía los datos.
            cursor.execute("INSERT INTO players (nickname, password) VALUES (?, ?)",
                           (nickEnt.get(), passwdEnt.get()))
            conectar.commit()
            infoLabel.config(text="Cuenta creada", fg="green")
            #Borra los campos.
            nickEnt.delete(0,tk.END)
            passwdEnt.delete(0,tk.END)
        #Si el nickname ya existe, salta excepción.
        except sqlite3.IntegrityError:
            infoLabel.config(text="El nombre ya está en uso", fg="red")
    else:
        infoLabel.config(text="Completa todos los campos", fg="red")
    conectar.close()

def createUser():
    global infoLabel
    newUser = tk.Tk()
    newUser.title("Ficha de jugador")
    newUser.geometry("200x100")
    newUser.resizable(False, False)
    
    userLabel = tk.Label(newUser, bg="#9db7e2")
    userLabel.grid(row=0, column=0)
    buttonBox = tk.LabelFrame(newUser, )
    buttonBox.grid(row=1, column=0)
    infoLabel = tk.Label(newUser, text="")
    infoLabel.grid(row=2, column=0)
    nickName = tk.Label(userLabel, text="Nombre: " , bg="#9db7e2")
    nickName.grid(row=0, column=0)
    nickEnt = tk.Entry(userLabel, )
    nickEnt.grid(row=0, column=1)
    playerPasswrd = tk.Label(userLabel, text="Contraseña: " , bg="#9db7e2")
    playerPasswrd.grid(row=1, column=0)
    passwrdEnt = tk.Entry(userLabel, show="*")
    passwrdEnt.grid(row=1, column=1)
    
    savePlayer = tk.Button(buttonBox, text="Guardar jugador", bg="#ffa31a", command=lambda: insertUser(nickEnt, passwrdEnt))
    savePlayer.grid(row=0, column= 0)
    exitCreate = tk.Button(buttonBox, text="Cancelar", bg="#ffa31a", command=lambda: exitUser(newUser))
    exitCreate.grid(row=0, column= 1)

def createDb():
    
    #Si la ruta no existe creas la carpeta
    if not os.path.exists(dbOriginDir):
        os.mkdir(dbOriginDir)

    initialdir = os.getcwd()
    path = initialdir + "/" + fullDbPath
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            nickname TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    connect.commit()
    connect.close() 
