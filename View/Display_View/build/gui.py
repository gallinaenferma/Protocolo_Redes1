
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

#PARTE GRAFICA DEL PROYECTO GUI

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Usuario\Desktop\Proyecto Redes 1\View\Display_View\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1379x850")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 850,
    width = 1379,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1379.0,
    850.0,
    fill="#474740",
    outline="")

canvas.create_rectangle(
    20.0,
    19.0,
    1019.0,
    209.0,
    fill="#ECE3E7",
    outline="")

canvas.create_rectangle(
    1039.0,
    19.0,
    1361.0,
    834.0,
    fill="#EDE3E8",
    outline="")

canvas.create_rectangle(
    20.0,
    224.0,
    1019.0,
    414.0,
    fill="#EDE3E8",
    outline="")

canvas.create_rectangle(
    20.0,
    434.0,
    1019.0,
    624.0,
    fill="#EDE3E8",
    outline="")

canvas.create_text(
    43.0,
    37.0,
    anchor="nw",
    text="TRANSMISOR",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    1115.0,
    34.0,
    anchor="nw",
    text="SECUENCIA DE TRAMAS",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_rectangle(
    20.0,
    644.0,
    1019.0,
    834.0,
    fill="#EDE3E8",
    outline="")

canvas.create_text(
    43.0,
    248.0,
    anchor="nw",
    text="RECEPTOR",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    475.0,
    277.0,
    anchor="nw",
    text="TRAMA RECIBIDA",
    fill="#000000",
    font=("Inter Medium", 14 * -1)
)

canvas.create_text(
    43.0,
    453.0,
    anchor="nw",
    text="RESPUESTA",
    fill="#000000",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    43.0,
    75.0,
    anchor="nw",
    text="Mensaje a transmitir:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    43.0,
    168.0,
    anchor="nw",
    text="Selección de semantica:",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    91.0,
    106.0,
    anchor="nw",
    text="DELIMITADOR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    179.0,
    495.0,
    anchor="nw",
    text="DELIMITADOR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    329.0,
    679.0,
    anchor="nw",
    text="SEMANTICA SELECCIONADA",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    443.0,
    717.0,
    anchor="nw",
    text="ESTADO",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    384.0,
    760.0,
    anchor="nw",
    text="MENSAJE RECIBIDO",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    265.0,
    351.0,
    anchor="nw",
    text="HEADER",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    588.0,
    351.0,
    anchor="nw",
    text="INFORMACIÓN",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    835.0,
    351.0,
    anchor="nw",
    text="TRAILER",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    539.0,
    106.0,
    anchor="nw",
    text="DATA",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    625.0,
    495.0,
    anchor="nw",
    text="DATA",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    692.0,
    106.0,
    anchor="nw",
    text="DELIMITADOR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    777.0,
    495.0,
    anchor="nw",
    text="DELIMITADOR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    226.0,
    106.0,
    anchor="nw",
    text="COF",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    226.0,
    106.0,
    anchor="nw",
    text="COF",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    319.0,
    495.0,
    anchor="nw",
    text="COF",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    270.0,
    106.0,
    anchor="nw",
    text="FIN",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    363.0,
    495.0,
    anchor="nw",
    text="FIN",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    310.0,
    106.0,
    anchor="nw",
    text="SOL",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    401.0,
    495.0,
    anchor="nw",
    text="SOL",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    349.0,
    106.0,
    anchor="nw",
    text="CTR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    443.0,
    495.0,
    anchor="nw",
    text="CTR",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    391.0,
    106.0,
    anchor="nw",
    text="PER",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    478.0,
    495.0,
    anchor="nw",
    text="PER",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    429.0,
    106.0,
    anchor="nw",
    text="NUM",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    516.0,
    495.0,
    anchor="nw",
    text="NUM",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    651.0,
    72.0,
    anchor="nw",
    text="Numero de frames",
    fill="#000000",
    font=("Inter", 13 * -1)
)

canvas.create_text(
    651.0,
    72.0,
    anchor="nw",
    text="Numero de frames",
    fill="#000000",
    font=("Inter", 13 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    373.5,
    79.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=190.0,
    y=68.0,
    width=367.0,
    height=21.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    128.0,
    139.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=43.0,
    y=128.0,
    width=170.0,
    height=21.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    223.0,
    527.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=138.0,
    y=516.0,
    width=170.0,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    406.0,
    330.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=295.0,
    y=319.0,
    width=222.0,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    634.0,
    330.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=523.0,
    y=319.0,
    width=222.0,
    height=21.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    862.0,
    330.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=751.0,
    y=319.0,
    width=222.0,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    178.0,
    330.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=67.0,
    y=319.0,
    width=222.0,
    height=21.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    555.0,
    139.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=470.0,
    y=128.0,
    width=170.0,
    height=21.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    642.0,
    528.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=557.0,
    y=517.0,
    width=170.0,
    height=21.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    603.0,
    686.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=518.0,
    y=675.0,
    width=170.0,
    height=21.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    603.0,
    724.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=518.0,
    y=713.0,
    width=170.0,
    height=21.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    603.0,
    767.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=518.0,
    y=756.0,
    width=170.0,
    height=21.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    736.0,
    139.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=651.0,
    y=128.0,
    width=170.0,
    height=21.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    822.0,
    527.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=737.0,
    y=516.0,
    width=170.0,
    height=21.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    239.0,
    139.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=224.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    332.0,
    527.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=317.0,
    y=516.0,
    width=30.0,
    height=21.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    280.0,
    139.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=265.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    373.0,
    527.5,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=358.0,
    y=516.0,
    width=30.0,
    height=21.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    321.0,
    139.5,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=306.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_20 = PhotoImage(
    file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(
    413.0,
    527.5,
    image=entry_image_20
)
entry_20 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_20.place(
    x=398.0,
    y=516.0,
    width=30.0,
    height=21.0
)

entry_image_21 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(
    362.0,
    139.5,
    image=entry_image_21
)
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_21.place(
    x=347.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_22 = PhotoImage(
    file=relative_to_assets("entry_22.png"))
entry_bg_22 = canvas.create_image(
    452.0,
    527.5,
    image=entry_image_22
)
entry_22 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_22.place(
    x=437.0,
    y=516.0,
    width=30.0,
    height=21.0
)

entry_image_23 = PhotoImage(
    file=relative_to_assets("entry_23.png"))
entry_bg_23 = canvas.create_image(
    403.0,
    139.5,
    image=entry_image_23
)
entry_23 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_23.place(
    x=388.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_24 = PhotoImage(
    file=relative_to_assets("entry_24.png"))
entry_bg_24 = canvas.create_image(
    490.0,
    528.5,
    image=entry_image_24
)
entry_24 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_24.place(
    x=475.0,
    y=517.0,
    width=30.0,
    height=21.0
)

entry_image_25 = PhotoImage(
    file=relative_to_assets("entry_25.png"))
entry_bg_25 = canvas.create_image(
    444.0,
    139.5,
    image=entry_image_25
)
entry_25 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_25.place(
    x=429.0,
    y=128.0,
    width=30.0,
    height=21.0
)

entry_image_26 = PhotoImage(
    file=relative_to_assets("entry_26.png"))
entry_bg_26 = canvas.create_image(
    531.0,
    527.5,
    image=entry_image_26
)
entry_26 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_26.place(
    x=516.0,
    y=516.0,
    width=30.0,
    height=21.0
)

entry_image_27 = PhotoImage(
    file=relative_to_assets("entry_27.png"))
entry_bg_27 = canvas.create_image(
    798.0,
    80.5,
    image=entry_image_27
)
entry_27 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_27.place(
    x=780.0,
    y=69.0,
    width=36.0,
    height=21.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=886.0,
    y=128.0,
    width=103.0,
    height=23.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=468.0,
    y=577.0,
    width=103.0,
    height=23.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=224.0,
    y=165.0,
    width=30.0,
    height=23.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=265.0,
    y=165.0,
    width=32.0,
    height=23.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=306.0,
    y=165.0,
    width=31.0,
    height=23.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=347.0,
    y=165.0,
    width=31.0,
    height=23.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=388.0,
    y=165.0,
    width=32.0,
    height=23.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=429.0,
    y=165.0,
    width=30.0,
    height=23.0
)

entry_image_28 = PhotoImage(
    file=relative_to_assets("entry_28.png"))
entry_bg_28 = canvas.create_image(
    1200.0,
    445.5,
    image=entry_image_28
)
entry_28 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_28.place(
    x=1058.0,
    y=75.0,
    width=284.0,
    height=739.0
)
window.resizable(False, False)
window.mainloop()