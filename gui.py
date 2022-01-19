from tkinter import *
import pyglet
from WillMusic import move_window


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def will_title(root):
    pyglet.font.add_file('assets/fonts/pexico.ttf')
    ctitle = Label(root, text="Wilbur Music", font=("Pexico-Regular", 40 * -1, "bold"), fg="black", bg="#c3c3c3",
                   height=3)
    ctitle.pack(fill=X)


def tbtns(title_bar, root):
    cbtnframe = Frame(title_bar, bg="navy")
    cbtnframe.pack(side=RIGHT, padx=3, pady=2)

    # put a close button on the title bar
    close_button = Button(cbtnframe, text=' ✕ ', fg="black", bg="#c3c3c3")
    close_button.configure(command=root.destroy, border=3)
    close_button.pack()

    minbtnframe = Frame(title_bar, bg="navy")
    minbtnframe.pack(side=RIGHT, padx=3, pady=2)

    # put a close button on the title bar
    close_button = Button(minbtnframe, text=' ✕ ', fg="black", bg="#c3c3c3")
    close_button.configure(command=root.destroy, border=3)
    close_button.pack()
