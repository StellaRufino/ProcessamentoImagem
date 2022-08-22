
from asyncio import events
from fileinput import filename
import io
from msilib.schema import ComboBox
from multiprocessing import Value
import os
from sqlite3 import Row
import PySimpleGUI as sg
from PIL import Image
import webbrowser
from copy import copy



def main():
    
    layout = [
        [sg.Image(key="-IMAGE-", size=(500,500)) ],
        [
            sg.Text("Arquivo de Imagem"),
            sg.Input(size=(20,1), key = "-FILE-"),
            sg.FileBrowse(file_types=[("JPEG(*.jpg)", "*jpg"), ("Todos os arquivos", "*.*")]),
            sg.Button("Carregar Imagem"),
            sg.Button("Salvar Imagem"),
            sg.Button("Salvar Thumb"),
            sg.Button("Salvar Sem Qualidade"),
            sg.Button("Pesquisar")
            
        ]
    ]

    salvarImg = 0;
    
    window = sg.Window("Visualizador de Imagem", layout = layout)
    while True:
        event, value = window.read()
        if event =="Exit" or event == sg.WINDOW_CLOSED:
            break
        if event == "Carregar Imagem":
            filename = value["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(filename)
                image.thumbnail((600,600))
                bio = io.BytesIO()
                image.save(bio,format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())

        # if event == "Salver Imagem":
        #     save_original(value["-FILE-"])
                
        if event == "Salvar Thumb":
            image_convert("calleri.jpg")#salvar thumbnail

        if event == "Salvar Sem Qualidade" :
            img_noQuality(value["-FILE-"], "calleri.png", "PNG")

        if event == "Pesquisar" :
            url_search(value["-FILE-"])
             
           
            


    window.close()



def image_convert(input_file):
    imagem = Image.open(input_file)  #abre
    imagem.thumbnail((75,75))
    imagem.save("thumbnail.jpg")


def img_noQuality(input_file, output_file, format):
    imagem = Image.open(input_file)  #abre
    imagem.save(output_file, format= format, optimize = True, quality = 1) #salva
    imagem.thumbnail((400,400))
    imagem.save("noQuality.jpg")
    
def format_select():
    combo = ComboBox()
    combo['values'] = ('jpg', 'png', 'GIF', 'bmp')

def url_search(url):
    webbrowser.open(url)

if __name__ == "__main__":
    main()
    
    



