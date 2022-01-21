from gui import *
from music import *
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    # Making the windows transparent while loading
    root.attributes('-alpha', 0.0)

    # Initializing the window
    root.title("WillMusic")
    root.iconbitmap("assets/will.ico")
    root.geometry("1200x650")
    root.configure(background='#c3c3c3', relief='raised', border=4)

    # Calling coustom title bar
    coustom_tbar(root)

    # Making the window at center
    center(root)

    # Title
    will_title(root)

    #music()

    root.minsize(1200, 650)
    root.attributes('-alpha', 1.0)  # Making the windows visible after loading

    root.mainloop()
