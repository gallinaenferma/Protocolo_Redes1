
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

#PARTE GRAFICA DEL PROYECTO GUI

from pathlib import Path

from Controller.Protocolo import Protocolo

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
# from Controller.Gui_Controller import btn_enviar
import tkinter as tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\PC\Desktop\Protocolo_Redes1\View\Display_View\build\assets\frame0")

protocolo = Protocolo()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
#1920*1080
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

# canvas.create_text(
#     329.0,
#     679.0,
#     anchor="nw",
#     text="SEMANTICA SELECCIONADA",
#     fill="#000000",
#     font=("Inter", 13 * -1)
# )

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

#ENTRADA MENSAJE A TRANSIMITR
entrada_mensaje = tk.StringVar()

entrada_mensaje = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_mensaje
)
entrada_mensaje.place(
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

#ENTRADA DELIMITADOR TRANSMISOR
entrada_del_trans = tk.StringVar()

entrada_delim_trans = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_del_trans
)
entrada_delim_trans.place(
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
#ENTRADA DELIMITADOR RESPUESTA
entrada_delim_respu=tk.StringVar()

entrada_delim_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_delim_respu
)
entrada_delim_resp.place(
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

# ENTRADA HEADER-2 RECEPTOR
# entrada_header2_recept=tk.StringVar()

entrada_header2_recep = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_header2_recept
)
entrada_header2_recep.config(state=tk.DISABLED)

entrada_header2_recep.place(
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
#ENTRADA INFORMACION RECEPTOR
# entrada_info_recep=tk.StringVar()

entrada_info_receptor = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_info_recep
)
entrada_info_receptor.config(state=tk.DISABLED)

entrada_info_receptor.place(
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
#ENTRADA TRAILER RECEPTOR
# entrada_trailer_recep=tk.StringVar()

entrada_trailer_receptor = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_trailer_recep
)
entrada_trailer_receptor.config(state=tk.DISABLED)

entrada_trailer_receptor.place(
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
#ENTRADA HEADER-1 RECEPTOR
# entrada_header1_recept=tk.StringVar()


entrada_header1_recep = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_header1_recept
)
entrada_header1_recep.config(state=tk.DISABLED)

entrada_header1_recep.place(
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
#ENTRADA DATA TRANSMISOR

entrada_data_transm = tk.StringVar()

entrada_data_trans = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_data_transm
)
entrada_data_trans.place(
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
#ENTRADA DATA RESPUESTA
entrada_data_respu=tk.StringVar()

entrada_data_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_data_respu
)
entrada_data_resp.place(
    x=557.0,
    y=517.0,
    width=170.0,
    height=21.0
)

# entry_image_10 = PhotoImage(
#     file=relative_to_assets("entry_10.png"))
# entry_bg_10 = canvas.create_image(
#     603.0,
#     686.5,
#     image=entry_image_10
# )
# #ENTRADA SEMANTICA SELLECIONADA
# entrada_sem_selecc=tk.StringVar()

# entrada_semantica_selecc = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0,
#     textvariable=entrada_sem_selecc
# )
# entrada_semantica_selecc.place(
#     x=518.0,
#     y=675.0,
#     width=170.0,
#     height=21.0
# )

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    603.0,
    724.5,
    image=entry_image_11
)
#ENTRADA ESTADO
# entrada_msj_estado=tk.StringVar()

entrada_msj_estad = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_msj_estado
)
entrada_msj_estad.config(state=tk.DISABLED)

entrada_msj_estad.place(
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
#ENTRADA MENSAJE RECIBIDO
#  entrada_msj_recibido=tk.StringVar()

entrada_msj_recib = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_msj_recibido
)
entrada_msj_recib.config(state=tk.DISABLED)


entrada_msj_recib.place(
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
#ENTRADA DELIMITADOR-2 TRANSMISOR
entrada_del2_trans=tk.StringVar()

entrada_delim2_resp  = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_del2_trans
)
entrada_delim2_resp .place(
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
#ENTRADA DELIMITADOR-2 RESPUESTA
entrada_delim2_respu=tk.StringVar()

entrada_delim2_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_delim2_respu
)
entrada_delim2_resp.place(
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

#LECTURA DE CAMPOS COF,FIN,SOL,CTR,PER Y NUM
entry_var = tk.StringVar()
entry_var_fin=tk.StringVar()
entry_var_sol=tk.StringVar()
entry_var_ctr=tk.StringVar()
entry_var_per=tk.StringVar()
entry_var_num=tk.StringVar()

#ENTRADA COF TRANSMISOR
entrada_cof = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var
)
entrada_cof.place(
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
#ENTRADA COF RESPUESTA
entrada_cof_respu = tk.StringVar()

entrada_cof_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_cof_respu
)
entrada_cof_resp.place(
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
#ENTRADA FIN TRANSMISOR
entry_17 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var_fin 
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
#ENTRADA FIN RESPUESTA
entrada_fin_respu=tk.StringVar()

entrada_fin_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_fin_respu
)
entrada_fin_resp.place(
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
#ENTRADA SOL TRANSMISION
entry_19 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var_sol
    
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

#ENTRADA SOL RESPUESTA
entrada_sol_respu=tk.StringVar() 

entrada_sol_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_sol_respu
)
entrada_sol_resp.place(
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
#ENTRADA CTR TRANSMISION
entry_21 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var_ctr
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
#ENTRADA CTR RESPUESTA
entrada_ctr_respu=tk.StringVar()

entrada_ctr_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_ctr_respu
)
entrada_ctr_resp.place(
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
#ENTRADA PER TRANSMISION
entry_23 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var_per
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
#ENTRADA PER RESPUESTA
entrada_per_respu=tk.StringVar() 

entrada_per_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_per_respu
)
entrada_per_resp.place(
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
#ENTRADA NUM TRANSMISOR
entrada_num_trans = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entry_var_num
)
entrada_num_trans.place(
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

#ENTRADA NUM RESPUESTA
entrada_num_respu=tk.StringVar()

entrada_num_resp = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_num_respu
)
entrada_num_resp.place(
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

#ENTRADA NUMERO DE FRAMES
entrada_frames = tk.StringVar()

entrada_num_frames = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable=entrada_frames
)
entrada_num_frames.place(
    x=780.0,
    y=69.0,
    width=36.0,
    height=21.0
)
#BOTON ENVIAR
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: btn_enviar(),
    relief="flat"
)

button_1.place(
    x=886.0,
    y=128.0,
    width=103.0,
    height=23.0
)

#BOTON RESPONDER
button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_responder(),
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

#BOTON COF
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_cof(),
    relief="flat"
)
button_3.place(
    x=224.0,
    y=165.0,
    width=30.0,
    height=23.0
)

#BOTON FIN
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_fin(),
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

#BOTON SOL
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_sol(),
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

#BOTON CTR
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_ctr(),
    relief="flat"
)
button_6.place(
    x=347.0,
    y=165.0,
    width=31.0,
    height=23.0
)
#BOTON PER
button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:btn_per(),
    relief="flat"
)
button_7.place(
    x=388.0,
    y=165.0,
    width=32.0,
    height=23.0
)

#BOTON NUM
button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: btn_num(),
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
#ENTRADA SECUENCIA DE TRAMAS

# entrada_sec_tramas=tk.Text()


entrada_sec_tram = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    # textvariable=entrada_sec_tramas,
    wrap=tk.WORD
)
entrada_sec_tram.config(state=tk.DISABLED)

entrada_sec_tram.place(
    x=1058.0,
    y=75.0,
    width=284.0,
    height=739.0,
    
)
#FUNCIONALIDADES BTN COF
def btn_cof():
    agg_eliminar_uno()
    print("Boton COF presionado")
   
    
    
def agg_eliminar_uno():
    contenido = entry_var.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var.set('') #borrar numero
    else:
        entry_var.set('1')
        
    
#FUNCIONALIDADES BTN FIN
def btn_fin():
    agg_eliminar_uno_fin()
    print("boton FIN presionado")
    

def agg_eliminar_uno_fin():
    contenido = entry_var_fin.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var_fin.set('') #borrar numero
    else:
        entry_var_fin.set('1')

#FUNCIONALIDADES BTN SOL 
def btn_sol():
    agg_eliminar_uno_sol()
    print("boton SOL presionado")
    

def agg_eliminar_uno_sol():
    contenido = entry_var_sol.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var_sol.set('') #borrar numero
    else:
        entry_var_sol.set('1')

       
#FUNCIONALIDADES BTN CRT
def btn_ctr():
    agg_eliminar_uno_ctr()
    print("boton CTR presionado")
    

def agg_eliminar_uno_ctr():
    contenido = entry_var_ctr.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var_ctr.set('') #borrar numero
    else:
        entry_var_ctr.set('1')

#FUNCIONALIDADES BTN PER

def btn_per():
    agg_eliminar_uno_per()
    print("boton PER presionado")
    

def agg_eliminar_uno_per():
    contenido = entry_var_per.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var_per.set('') #borrar numero
    else:
        entry_var_per.set('1')

#FUNCIONALIDADES BTN NUM

def btn_num():
    agg_eliminar_uno_num()
    print("boton NUM presionado")
    

def agg_eliminar_uno_num():
    contenido = entry_var_num.get()# Obtener el contenido del campo de texto
    if contenido.isdigit():  # Verificar si el contenido es un número
        entry_var_num.set('') #borrar numero
    else:
        entry_var_num.set('1')

###FUNCIONALIDADES BOTON ENVIAR###
def btn_enviar():
    mensaje_enviar = leer_campo_mensaje()
    num_frames = leer_num_frames()

    protocolo.mensaje_transmitir = protocolo.dividir_cadena(mensaje_enviar,num_frames)

    delim_inicial = leer_campo_delim_trans()
    cof = leer_campo_cof_trans()
    fin = leer_campo_fin_trans()
    sol = leer_campo_sol_trans()
    ctr = leer_campo_ctr_trans()
    per = leer_campo_per_trans()
    num = leer_campo_num_trans()
    data = leer_campo_data_trans()
    delimitador_final = leer_campo_del2_trans()

    trama = protocolo.crear_trama(delim_inicial,cof,fin, sol,ctr,per,num,data,delimitador_final)
    mensaje = protocolo.enviar_trama(trama)
    mostar_msj_sec_tramas(mensaje)
    print("El mensaje es: ", mensaje)


###FUNCIONALIDADES BOTON RESPONDER###
def btn_responder():

    delimitador_inicial = leer_campo_delim_resp()
    cof = leer_campo_cof_resp()
    fin = leer_campo_fin_resp()
    sol = leer_campo_sol_resp()
    ctr = leer_campo_ctr_resp()
    per = leer_campo_per_resp()
    num = leer_campo_num_resp()
    data = leer_campo_data_resp()
    delimitador_final = leer_campo_delim2_resp()

    trama = protocolo.crear_trama(delimitador_inicial,cof,fin,sol,ctr,per,num,data,delimitador_final)
    mensaje = protocolo.responder_trama(trama)
    print("Tramas recibidas: ", protocolo.tramas_recibidas)
    mostar_msj_sec_tramas(mensaje)

    print("Delimitador inicial: ", delimitador_inicial)
    print("COF: ", cof)
    print("Tipo FIN: ", type(fin))
    print("Tipo SOL: ", type(sol))
    print("Tipo CTR: ", type(ctr))
    print("Tipo PER: ", type(per))
    print("Tipo NUM: ", type(num))
    print("Data: ", data)
    print("Delimitador final: ", delimitador_final)


      


###########################SECCION TRANSMISOR#######################

def leer_campo_mensaje():#campo de texto donde se escribe el mensaje
    contenido = entrada_mensaje.get()
    print(contenido)
    return contenido

def leer_num_frames():#campo donde se ecriben la cantidad de frames
    contenido = entrada_frames.get()
    print(contenido)
    return int(contenido)


def leer_campo_delim_trans():#campo de texto donde se escribe el delimitador-1 en transmisor
    contenido = entrada_del_trans.get()
    print(contenido)
    return contenido

def leer_campo_data_trans():
    contenido = entrada_data_transm.get()
    print(contenido)
    return contenido
    
def leer_campo_del2_trans():#campo de texto donde se escribe el delimitador-2 en transmisor
    contenido = entrada_del2_trans.get()
    print(contenido)
    return contenido



def leer_campo_cof_trans():#campo de texto donde se pone el numero COF
    contenido = entry_var.get()
    print(contenido)
    return int(contenido)

def leer_campo_fin_trans():#campo de texto donde se pone el numero FIN
    contenido = entry_var_fin.get()
    print(contenido)
    return int(contenido)

def leer_campo_sol_trans():#campo de texto donde se pone el numero SOL
    contenido = entry_var_sol.get()
    print(contenido)
    return int(contenido)
    
def leer_campo_ctr_trans():#campo de texto donde se pone el numero CTR
    contenido = entry_var_ctr.get()
    print(contenido)
    return int(contenido)
    
def leer_campo_per_trans():#campo de texto donde se pone el numero PER
    contenido = entry_var_per.get()
    print(contenido)
    return int(contenido)

def leer_campo_num_trans():#campo de texto donde se pone el numero NUM
    contenido = entry_var_num.get()
    print(contenido)
    return int(contenido)

###########################SECCION RECEPTOR#######################


#dato es la variable que viene desde la logica
def leer_campo_head1_recep(dato):
    entrada_header1_recep.config(state=tk.NORMAL)
    contenido=entrada_header1_recep.insert(tk.END,dato)
    entrada_header1_recep.config(state=tk.DISABLED)
    print(contenido)
  
def leer_campo_head2_recep(dato):
    entrada_header2_recep.config(state=tk.NORMAL)
    # msj="como fue?"
    contenido=entrada_header2_recep.insert(tk.END,dato)
    entrada_header2_recep.config(state=tk.DISABLED)
    print(contenido)

def leer_campo_info_recep(dato):
    entrada_info_receptor.config(state=tk.NORMAL)
    # msj="hola rey"
    contenido=entrada_info_receptor.insert(tk.END,dato)
    entrada_info_receptor.config(state=tk.DISABLED)
    print(contenido)
    
def leer_campo_trailer_recep(dato):
    entrada_trailer_receptor.config(state=tk.NORMAL)
    # msj="hola moor"
    contenido=entrada_trailer_receptor.insert(tk.END,dato)
    entrada_trailer_receptor.config(state=tk.DISABLED)
    print(contenido)

###########################SECCION RESPUESTA#######################

def leer_campo_delim_resp():
    contenido=entrada_delim_respu.get()
    print(contenido)
    return contenido
    
def leer_campo_cof_resp():
    contenido=entrada_cof_respu.get()
    print(contenido)
    return int(contenido)

def leer_campo_fin_resp():
    contenido=entrada_fin_respu.get()
    print(contenido)
    return int(contenido)

def leer_campo_sol_resp():
    contenido=entrada_sol_respu.get()
    print(contenido)
    return int(contenido)

def mostar_msj_sec_tramas(mensaje):
    entrada_sec_tram.config(state=tk.NORMAL)
    # mensaje="(TX) Control, solicitud permiso para transmitir" #poner por variable a mostrar
    contenido=entrada_sec_tram.insert(tk.END,mensaje+"\n")
    entrada_sec_tram.config(state=tk.DISABLED)
    print(contenido)

def leer_campo_ctr_resp():
    contenido=entrada_ctr_respu.get()
    print(contenido)
    return int(contenido)

def leer_campo_per_resp():
    contenido=entrada_per_respu.get()
    print(contenido)
    return int(contenido)

def leer_campo_num_resp():
    contenido=entrada_num_respu.get()
    print(contenido)
    return int(contenido)

def leer_campo_data_resp():
    contenido=entrada_data_respu.get()
    print(contenido)
    return contenido

def leer_campo_delim2_resp():
    contenido=entrada_delim2_respu.get()
    print(contenido)
    return contenido
###########################SECCION RESPUESTA TRAMAS######################

###########################SECCION RESULTADO FINAL#######################

# def mostar_msj_sem_selecc():
#     numero='1'
#     cof=entry_var.get()
#     fin=entry_var_fin.get()
#     sol=entry_var_sol.get()
#     ctr=entry_var_ctr.get()
#     per=entry_var_per.get()
#     num=entry_var_num.get()
    

#     if  cof == numero:
#         mensaje="COF"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido
#     elif fin == numero:
#         mensaje="FIN"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido
#     elif sol == numero:
#         mensaje="SOL"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido
#     elif ctr == numero:
#         mensaje="CTR"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido
#     elif per == numero:
#         mensaje="PER"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido
#     elif num == numero:
#         mensaje="NUM"
#         contenido=entrada_sem_selecc.set(mensaje)
#         return contenido


def mostar_msj_estado(mensaje):
    # ESPERAR CONDICION
    # if:
    # mensaje="Exitoso" #poner por variable a mostrar
    # contenido=entrada_msj_estado.set(mensaje)
    # else
    # mensaje="Fallido" #poner por variable a mostrar
    # contenido=entrada_msj_estado.set(mensaje)
    entrada_msj_estad.config(state=tk.NORMAL)
    # mensaje="(TX) Control" #poner por variable a mostrar
    contenido=entrada_msj_estad.insert(tk.END,mensaje+"\n")
    entrada_msj_estad.config(state=tk.DISABLED)
    print(contenido)

def mostar_msj_recibido(mensaje):
    entrada_msj_recib.config(state=tk.NORMAL)
    # mensaje="Hola moor" #poner por variable a mostrar
    contenido=entrada_msj_recib.insert(tk.END,mensaje+"\n")
    entrada_msj_recib.config(state=tk.DISABLED)
    
    print(contenido)

window.resizable(False, False)
window.mainloop()




