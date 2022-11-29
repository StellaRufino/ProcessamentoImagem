
import io
import os
from turtle import color
import PySimpleGUI as sg
from PIL import Image
import requests
from PIL import ImageFilter
from PIL.ExifTags import TAGS, GPSTAGS
from pathlib import Path
import webbrowser
from PIL import ImageEnhance
import shutil
import tempfile

sg.theme("DarkRed")


barra_menu = [
['Arquivo', ['Carregar', 'URL']],

['Salvar', ['Sem qualidade','Thumbnail',
'Formatos',['BMP','JPEG', 'PNG']]],

['Filtros',['Blur',['BoxBlur','GaussianBlur', 'SBlur'],'Efeitos',['Brilho','Contraste','Cores','Nitidez', 'Preto/Branco','Quantidade de Cores','Sem Efeitos','Sepia'
'Contour','Detail','Edge Enhance','Emboss','Find Edges','Sharpen','Smooth']]],

['Editar',['Espelhar',['FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','TRANSPOSE'],'Recortar','Redimensinar']],

['Ajuda', ['MetaDados','Localização']]

]

tmp_file = tempfile.NamedTemporaryFile(suffix=".png").name

def main():
    
    layout = [
            [sg.Menu(barra_menu)],
     
            [sg.Graph(key="-IMAGE-", canvas_size=(800,600), graph_bottom_left=(0, 0),
                    graph_top_right=(400, 500), change_submits=True, drag_submits=True)],
            
        ]
        
    
    window = sg.Window("Visualizador de Imagem", layout = layout)
    while True:
        event, value = window.read()
        if event =="Exit" or event == sg.WINDOW_CLOSED:
            break                

        if event in ["Carregar","Carregar URL"]:
               filename = open_image(tmp_file,event,window)    
                      
        if event == "Salvar Thumb":
            image_convert("calleri.jpg")#salvar thumbnail

        if event == "Salvar Sem Qualidade" :
            img_noQuality(value["-FILE-"], "calleri.png", "PNG")

        if event == "Pesquisar" :
            url_search(value["-FILE-"])

        if event == "Formato" :
            textBox = value["-FORMAT-"]   
            
        if event == "Sobre":
                openInfoWindow(filename,window)
        if event == "Localização":
                GPS(filename)        
           
            
    window.close()


def image_convert(input_file):
    imagem = Image.open(input_file)  #abre
    imagem.thumbnail((75,75))
    imagem.save("thumbnail.jpg")


def img_noQuality(input_file, output_file, format):
    imagem = Image.open(input_file)  #abre
    imagem.save(output_file, format= format, optimize = True, quality = 1) #salva
    imagem.thumbnail((600,600))
    imagem.save("noQuality.jpg")
    
def format_select(formato):
    formato = formato['values'] = ('jpg', 'png', 'GIF', 'bmp')
    

def url_search(url):
    webbrowser.open(url)

def open_image(temp_file,event,window):
        if event == "Carregar":
            filename = sg.popup_get_file('Carregue sua imagem')
            image = Image.open(filename)
            image.save(temp_file)
            mostrar_imagem(image, window)
        else:
            url = sg.popup_get_text("URL")
            image = requests.get(url)
            image = Image.open(io.BytesIO(image.content))
            temp_image2 = image.copy()
            temp_image2.save("temp.png",format = "PNG",optmize = True)
            mostrar_imagem(image, window)
        return filename

def mostrar_imagem(imagem, window):
    bio = io.BytesIO()
    imagem.save(bio, "PNG")
    window["-IMAGE-"].erase()
    window["-IMAGE-"].draw_image(data=bio.getvalue(), location=(0,400))            

if __name__ == "__main__":
    main()
    
    

