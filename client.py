import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import ntpath
import time
from ftplib import FTP
from tkinter import filedialog
from pathlib import Path
from playsound import playsound
import pygame
from pygame import mixer
from PIL import ImageTk, Image


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
screen_width = None
screen_height = None
name = None
listbox =  None
filePathLabel = None

global song_counter
song_counter = 0

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)
    
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: " +song_selected)
    else:
        infoLabel.configure(text="")

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    
    mixer.music.unpause() 

def musicWindow(): 
    global song_counter
    global filePathLabel
    global listbox
    global infoLabel
    global screen_width
    global screen_height
    
    window  = Tk()
    window.title("Music Sharing App!!")


    bg = ImageTk.PhotoImage(file = "download.png")

    canvas1 = Canvas( window, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    canvas1.create_image(0,0, image = bg, anchor = "nw")
    
    selectlabel = Label(window, text= "Select Song",bg='cyan', font = ("Calibri",8))
    selectlabel.place(x=50, y=1)
    
    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg='yellow',borderwidth=2, font = ("Calibri",10))
    listbox.place(x=50,y=18)
    for file in os.listdir('shared_files'):
        filename = os.fsdecode(file)
        listbox.insert(song_counter, filename)
        song_counter = song_counter + 1
        
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton=Button(window,text="Play", width=20 , height=5,bd=1,bg='blue',font = ("Calibri",10), command = play)
    PlayButton.place(x=30,y=200)
    
    Stop=Button(window,text="Stop",bd=1,width=20 , height=5,bg='blue', font = ("Calibri",10), command = stop)
    Stop.place(x=200,y=200)

    Upload=Button(window,text="Upload",width=20 , height=5,bd=1,bg='green', font = ("Calibri",10))
    Upload.place(x=30,y=300)
    
    Download =Button(window,text="Download",width=20 , height=5,bd=1,bg='green', font = ("Calibri",10))
    Download.place(x=200,y=300)
    
    infoLabel = Label(window, text= "",fg= "blue",bg='yellow', font = ("Calibri",8))
    infoLabel.place(x=4, y=330)
    
    window.resizable(True, True)

    window.mainloop()
    
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS
    global song_counter

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()

setup()