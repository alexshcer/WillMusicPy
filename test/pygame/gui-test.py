from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../../assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1200x600")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.resizable(True, True)
window.mainloop()


"""


canvas = Canvas(
    window,
    bg = "#333333",
    height = 900,
    width = 1600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    440.0,
    66.0,
    anchor="nw",
    text="Willbur Soot Music",
    fill="#FFFFFF",
    font=("PetronaRoman Regular", 40 * -1)

)

canvas.create_rectangle(
    625.0,
    221.0,
    975.0,
    571.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    700.0,
    708.0,
    900.0,
    748.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1529.0,
    26.0,
    1569.0,
    66.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    501.0,
    779.0,
    1101.0,
    803.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    1542.0,
    76.0,
    1557.0,
    221.0,
    fill="#000000",
    outline="")
"""