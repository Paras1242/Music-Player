import pygame
import os
from pygame import mixer
from tkinter import *


def play_song():
    currentSong = playlist.get(ACTIVE)
    print("You selected: ", currentSong)

    resume_btn.pack_forget()

    mixer.music.load(currentSong)
    SongStatus.set("Playing")
    mixer.music.play()
    pause_btn.pack(side = LEFT, expand = True, fill = BOTH)

def pause_song():
    resume_btn.pack(side = LEFT, expand = True, fill = BOTH)
    SongStatus.set("Paused")
    mixer.music.pause()
    pause_btn.pack_forget()
    

def stop_song():
    resume_btn.pack_forget()
    SongStatus.set("Stopped")
    mixer.music.stop()
    pause_btn.pack(side = LEFT, expand = True, fill = BOTH)

def resume_song():
    SongStatus.set("Resuming")
    mixer.music.unpause()
    resume_btn.pack_forget()
    pause_btn.pack(side = LEFT, expand = True, fill = BOTH)



window = Tk()
window.title('Music player project')

mixer.init()

SongStatus = StringVar()
SongStatus.set("choosing")

# create playlist

playlist = Listbox(window, selectmode=SINGLE, bg="cyan",fg="black",font=('arial',15),width=40)
playlist.pack(side = LEFT, expand = True, fill = BOTH)
# playlist.grid(columnspan=5)

os.chdir(r'C:\Users\HP\Desktop\Music Player\music')
songs = os.listdir()

for song in songs:
    playlist.insert(END,song)


play_btn = Button(window, text="Play", command=play_song)
play_btn.config(font=('arial',20), bg="black",fg="cyan",padx=7,pady=7)
play_btn.pack(side = LEFT, expand = True, fill = BOTH)
# play_btn.grid(row=1,column=0)

pause_btn = Button(window, text="Pause", command=pause_song)
pause_btn.config(font=('arial',20), bg="black",fg="cyan",padx=7,pady=7)
pause_btn.pack(side = LEFT, expand = True, fill = BOTH)
# pause_btn.grid(row=1,column=1)

stop_btn = Button(window, text="Stop", command=stop_song)
stop_btn.config(font=('arial',20), bg="black",fg="cyan",padx=7,pady=7)
stop_btn.pack(side = LEFT, expand = True, fill = BOTH)
# stop_btn.grid(row=1,column=2)

resume_btn = Button(window, text="Resume", command=resume_song)
resume_btn.config(font=('arial',20), bg="black",fg="cyan",padx=7,pady=7)
resume_btn.pack(side = LEFT, expand = True, fill = BOTH)
# resume_btn.grid(row=1,column=3)

window.mainloop()