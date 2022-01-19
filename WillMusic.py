import tkinter as tk
from gui import *
from music import *


def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


if __name__ == '__main__':
    root = tk.Tk()

    root.attributes('-alpha', 0.0)  # Making the windows transparent while loading

    # Giving the theme
    # style = ttk.Style(root)
    ## Importing the tcl
    # root.tk.call("source", "assets/theme/WillMusicTheme.tcl")
    ## Using the theme from WillMusicTheme folder
    # style.theme_use("WillMusicTheme")

    # Initializing the window
    root.title("WillMusic")
    root.iconbitmap("assets/will.ico")
    root.geometry("1200x650")
    root.configure(background='#c3c3c3', relief='raised', border=4)

    # Making Title Bar Change
    root.overrideredirect(True)  # turns off title bar, geometry

    # make a frame for the title bar
    title_bar = Frame(root, bg='navy')
    # put a close button on the title bar
    tbtns(title_bar, root)
    # Title Label
    tlabel = Label(title_bar, font=("MS Sans Serif", 12, "bold",), text="Willbur Soot", bg="navy",
                   fg="gainsboro", padx=4)

    # pack the widgets
    title_bar.pack(fill=X)
    tlabel.pack(side=LEFT)

    # bind title bar motion to the move window function
    tlabel.bind('<B1-Motion>', move_window)
    title_bar.bind('<B1-Motion>', move_window)

    # Making the window at center
    center(root)

    # Title
    will_title(root)
    # Calling Music
    # music()

    root.minsize(1200, 650)
    root.attributes('-alpha', 1.0)  # Making the windows visible after loading

    root.mainloop()
