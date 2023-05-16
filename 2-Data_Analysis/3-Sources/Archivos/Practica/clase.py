import os
import shutil

class Fichero:

    def __init__(self, carpeta, extensions, ruta):
        self.carpeta = carpeta
        self.extensions = extensions
        self.ruta = ruta
        self.select_dir()
        self.create_dir()
        self.move_file()


    def select_dir(self):
        os.chdir(self.ruta)

    def create_dir(self):
        os.makedirs(self.carpeta, exist_ok=True)

    def move_file(self):
        for archivo in os.listdir():
            if os.path.isdir(archivo):
                print(archivo, "es una carpeta")
            elif self.extensions==None or archivo.endswith(self.extensions):
                shutil.move(archivo, self.carpeta)