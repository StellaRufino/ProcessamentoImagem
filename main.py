
from multiprocessing.sharedctypes import Value
from turtle import position
import PySimpleGUI as sg
import os
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
        if event == "Carregar Imagem":
            filename = value["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(filename)
                image.thumbnail((600,600))
                bio = io.BytesIO()
                image.save(bio,format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())

                      
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

if __name__ == "__main__":
    main()
    
    

