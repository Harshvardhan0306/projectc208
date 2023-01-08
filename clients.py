import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    window = Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg = 'LightSkyBlue')

    selectlabel = Label(window, text = "Select Song", bg = "LightSkyBlue", font = ("Calbiri", 0))
    selectlabel.place(x = 2, y = 1)

    listbox = Listbox(window, height = 10, width = 35, activestyle = 'dotbox', bg = "LightSkyBlue", borderwidth = 2, font = ("calbiri", 10))
    listbox.place(x = 10, y = 10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = listbox.yview)

    playbutton = Button(window, text = "Play", width = 10, bd = 1, bg = "skyBlue", font = ("Calbiri", 10))
    playbutton.place(x = 30, y = 200)

    stop = Button(window, text = "Stop", width = 10, bd = 1, bg = "skyBlue", font = ("Calbiri", 10))
    stop.place(x = 200, y = 200)

    upload = Button(window, text = "Upload", width = 10, bd = 1, bg = "skyBlue", font = ("Calbiri", 10))
    upload.place(x = 30, y = 250)

    download = Button(window, text = "Download", width = 10, bd = 1, bg = "skyBlue", font = ("Calbiri", 10))
    download.place(x = 200, y = 250)

    infolabel = Label(window, text = "", bg = "LightSkyBlue", font = ("Calbiri", 10))
    infolabel.place(x = 2, y = 1)

    window.mainloop()

def setup():
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()


setup()