import os
import shutil
from variables import *

def select_dir(carpeta):
    os.chdir(carpeta)

def create_dirs():
    os.makedirs("Imagenes", exist_ok=True)
    os.makedirs("Documentos", exist_ok=True)
    os.makedirs("Softwares", exist_ok=True)
    os.makedirs("Otros", exist_ok=True)

def move_files():
    for archivo in os.listdir():
        if os.path.isdir(archivo):
            print(archivo, "es una carpeta")
        elif archivo.endswith(doc_types):
            print(archivo, "es un documento")
            shutil.move(archivo, "Documentos")
        elif archivo.endswith(img_types):
            print(archivo, "es una imagen")
            shutil.move(archivo, "Imagenes")
        elif archivo.endswith(software_types):
            print(archivo, "es un software")
            shutil.move(archivo, "Softwares")
        else:
            print(archivo, "es otro tipo de extension")
            shutil.move(archivo, "Otros")
            