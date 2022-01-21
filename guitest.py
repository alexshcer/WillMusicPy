from tkinter import *
from ctypes import windll
import pyglet


def set_appwindow(mainWindow):  # to display the window icon on the taskbar,
    # even when using root.overrideredirect(True)

    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())


def coustom_tbar(root):
    # Making Title Bar Change
    root.overrideredirect(True)  # turns off title bar, geometry

    # make a frame for the title bar
    title_bar = Frame(root, bg='navy')
    # Title Label
    tlabel = Label(title_bar, font=("MS Sans Serif", 12, "bold",), text="Willbur Soot", bg="navy",
                   fg="gainsboro", padx=4)

    # Putting buttons on the title bar
    tbtns(title_bar, tlabel, root)

    # pack the widgets
    title_bar.pack(fill=X)
    tlabel.pack(side=LEFT)


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


def tbtns(title_bar, tlabel, root):
    root.minimized = False  # only to know if root is minimized
    root.maximized = False  # only to know if root is maximized

    def minimize_me():
        # so you can't see the window when is minimized
        root.attributes("-alpha", 0)
        root.minimized = True

    def deminimize(event):

        root.focus()
        # so you can see the window when is not minimized
        root.attributes("-alpha", 1)
        if root.minimized == True:
            root.minimized = False

    def maximize_me():

        if root.maximized == False:  # if the window was not maximized
            root.normal_size = root.geometry()
            max_button.config(text=" 🗗 ")
            root.geometry(
                f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
            root.maximized = not root.maximized
            # now it's maximized

        else:  # if the window was maximized
            max_button.config(text=" 🗖 ")
            root.geometry(root.normal_size)
            root.maximized = not root.maximized
            # now it is not maximized

    # put a close button on the title bar
    cbtnframe = Frame(title_bar, bg="navy")
    cbtnframe.pack(side=RIGHT, padx=3, pady=2)

    close_button = Button(cbtnframe, text=' ✕ ', fg="black", bg="#c3c3c3")
    close_button.configure(command=root.destroy, border=3)
    close_button.pack()

    # put a maximize button on the title bar
    maxbtnframe = Frame(title_bar, bg="navy")
    maxbtnframe.pack(side=RIGHT, padx=3, pady=2)

    max_button = Button(maxbtnframe, text=' 🗖 ', fg="black", bg="#c3c3c3")
    max_button.configure(command=maximize_me, border=3)
    max_button.pack()

    # put a minimize button on the title bar
    minbtnframe = Frame(title_bar, bg="navy")
    minbtnframe.pack(side=RIGHT, padx=3, pady=2)

    min_button = Button(minbtnframe, text=' 🗕 ', fg="black", bg="#c3c3c3")
    min_button.configure(command=minimize_me, border=3)
    min_button.pack()

    def get_pos(event):  # this is executed when the title bar is clicked to move the window

        if root.maximized == False:
            xwin = root.winfo_x()
            ywin = root.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(event):  # runs when window is dragged
                # root.config(cursor="None")
                root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

            def release_window(event):  # runs when window is released
                root.config(cursor="arrow")

            title_bar.bind('<B1-Motion>', move_window)
            title_bar.bind('<ButtonRelease-1>', release_window)
            tlabel.bind('<B1-Motion>', move_window)
            tlabel.bind('<ButtonRelease-1>', release_window)
        else:
            max_button.config(text=" 🗖 ")
            root.maximized = not root.maximized

    # so you can drag the window from the title bar
    title_bar.bind('<Button-1>', get_pos)
    # so you can drag the window from the title
    tlabel.bind('<Button-1>', get_pos)
    root.bind("<FocusIn>", deminimize)
    # to see the icon on the task bar
    root.after(10, lambda: set_appwindow(root))
