from email.mime import image
from pickletools import optimize
from PIL import Image

# imagem = Image.open('trikas.jpeg')
# imagem.show("Trikas")

def image_convert(input_file, output_file, format):
    imagem = Image.open(input_file)  #abre
    imagem.save(output_file, format= format, optimize = True, quality = 1) #salva
    imagem.thumbnail((75,75))
    imagem.save("thumbnail.jpg")

def image_format(input_file):
    imagem = Image.open(input_file) #abre
    print(f"Formato: {imagem.format_description}") #f para entender que é uma interpolação

if __name__ == "__main__":
    image_convert("trikas.jpeg", "trikas.png", "PNG")
    image_convert("trikas.png", "trikas.jpg", "JPEG")
    image_format("trikas.jpeg")
    image_format("trikas.png")
    image_format("trikas.spfc")







