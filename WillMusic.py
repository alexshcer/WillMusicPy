from tkinter import *
import tkinter as tk
import pygame as pg

root = tk.Tk()
root.title("Willbur Soot Music")
root.iconbitmap("will.ico")
root.geometry("500x400")

pg.mixer.init()

def onload():
    play()

MUSIC_END = pg.USEREVENT+1
running = False
def play():
    i=1
    pg.mixer.music.load(f"audio/{i}.mp3")
    pg.mixer.music.set_volume(0.8)
    pg.mixer.music.play(loops=2)
    pg.mixer.music.set_endevent(MUSIC_END)
    i += 1
    running = True

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == MUSIC_END:
            print('music end event')
            play()

        if event.type == pg.MOUSEBUTTONDOWN:
            # play again
            pg.mixer.music.play()

root.after(2000, onload)
root.mainloop()
