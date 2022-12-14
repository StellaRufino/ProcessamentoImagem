from asyncio import events

from fileinput import filename
import io
from linecache import lazycache
from multiprocessing import Value
import os
from tkinter import image_names
from tkinter.tix import WINDOW
import PySimpleGUI as sg
from PIL import Image

def main():
    layout = [
        [sg.Image(key="-IMAGE-", size=(500,500)) ],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(25,1), key = "-FILE-"),
            sg.FileBrowse(file_types=[("JPEG(*.jpg)", "*jpg"), ("Todos os arquivos", "*.*")]),
            sg.Button("Carregar Imagem")
        ]
    ]

    window = sg.Window("Visualizador de Imagem", layout = layout)
    while True:
        event, value = window.read()
        if event =="Exit" or event == sg.WINDOW_CLOSED:
            break
        if event == "Carregar Imagem":
            filename = value["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(filename)
                image.thumbnail((500,500))
                bio = io.BytesIO()
                image.save(bio,format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())

    window.close()


if __name__ == "__main__":
    main()