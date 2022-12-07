from multiprocessing.sharedctypes import Value
from turtle import position
import PySimpleGUI as sg
import os
from funcoes import *
import tempfile

sg.theme("DarkRed")

menu_def = [
['Arquivo', ['Carregar', 'URL']],

['Salvar', ['Sem qualidade','Thumbnail',
'Formatos',['BMP','JPEG', 'PNG']]],

['Filtros',['Blur',['BoxBlur','GaussianBlur', 'SBlur'],'Efeitos',['Brilho','Contraste','Cores','Nitidez', 'Preto/Branco','Quantidade de Cores','Sem Efeitos','Sepia'
'Contour','Detail','Edge Enhance','Emboss','Find Edges','Sharpen','Smooth']]],

['Editar',['Espelhar',['FLIP_LEFT_RIGHT','FLIP_TOP_BOTTOM','TRANSPOSE'],'Recortar','Redimensinar']],

['Ajuda', ['MetaDados','Localização']]


]

esquerda=[
  [sg.Frame(
          layout=[
            [sg.Graph(key="-IMAGE-", canvas_size=(500,500), graph_bottom_left=(0, 0),
              graph_top_right=(400, 400), change_submits=True, drag_submits=True)],
          ],
        title="",
        relief=sg.RELIEF_GROOVE,
          )
        ],
]

direita = [
  [sg.Frame(
          layout=[
            [sg.Slider(range=(0, 5), default_value=2, resolution=0.1, orientation="h", enable_events=True, disabled= True,key="-SLIDER-")],
            [sg.Text('X,Y INI:',text_color='WHITE',key="-INI-")],
            [sg.Text('X,Y END:',text_color='WHITE',key="-END-")],
            ],
          title="",
          relief=sg.RELIEF_GROOVE,
          key="-FRAME_POSITION-",
          )
        ],
      [sg.Button("Sobre", disabled=True, key="Metadados"),sg.Button("GPS", disabled=True, key="Localização")],
]

ld_esq = sg.Column(esquerda)

tmp_file = tempfile.NamedTemporaryFile(suffix=".png").name

def main():
    layout = [
        [sg.Menu(menu_def, background_color="DarkRed", text_color="white")],
        [ld_esq,
          sg.VSeperator(pad=(0, 0)),
          sg.Column(direita),
        ],
    ]
    window = sg.Window("Photoshop Pobre",layout = layout, size=(750,500))
    dragging = False
    ponto_INI = filename = ponto_END = retangulo = None
    actualeffect = ''
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        try:
            if event in ["Carregar","URL"]:
                filename = abre_imagem(tmp_file,event,window)
                

            if event == "Redimensionar":
                x = int(sg.popup_get_text("Coloque X"))
                y = int(sg.popup_get_text("Coloque Y"))
                resize(tmp_file,"RedimImage.png",(x,y))

            if event == "Thumbnail":
                save_thumbnail(tmp_file,"Thumbnail.png","png",75,75,75)

            if event == "Sem qualidade":
                save_reduzida(tmp_file,"Reduzida.png")
                
            if event in ["JPEG","PNG","BMP"]:
                image_converter(tmp_file,'saved',event)
    
            if event == "Metadados":
                openInfoWindow(filename,window)
            if event == "Localização":
                GPS(filename)

            if event in ["Normal","P/B","QTD Cor","Sepia",
            'Brilho','Cores','Contraste','Nitidez']:
                actualeffect = event
                window.Element("-SLIDER-").update(disabled = False,value = 2)
                applyEffect(filename,tmp_file,actualeffect,values,window)

                

            if event in ['SBlur','BoxBlur','GaussianBlur','Contour',
            'Edge Enhance','Emboss','Find Edges',
            'TRANSPOSE','FLIP_TOP_BOTTOM','FLIP_LEFT_RIGHT']:
                filter(tmp_file,event,window)

            if event == "-SLIDER-":
               applyEffect(filename,tmp_file,actualeffect,values,window)
            
            if event == "-IMAGE-":
                x, y = values["-IMAGE-"]
                if not dragging:
                    ponto_INI = (x, y)
                    dragging = True
                else:
                    ponto_END = (x, y)
                if retangulo:
                    window["-IMAGE-"].delete_figure(retangulo)
                if None not in (ponto_INI, ponto_END):
                    retangulo = window["-IMAGE-"].draw_rectangle(ponto_INI, ponto_END, line_color='red')
                    
                    window.Element('-INI-').update(f'{ponto_INI}')
                    window.Element('-END-').update(f'{ponto_END}')
                    
                    
                
            elif event.endswith('+UP'):
                dragging = False
    
    
        except Exception as e:
            sg.popup_error(e)

    window.close()


if __name__ == "__main__":
    main()