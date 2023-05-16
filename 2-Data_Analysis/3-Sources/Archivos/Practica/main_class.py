import os
from variables import *
from clase import Fichero


ruta = os.path.dirname(os.path.abspath(__file__))+"/descargas_test"

documentos = Fichero("Documentos", doc_types, ruta)
imagenes = Fichero("Imagenes", img_types, ruta)
softwares = Fichero("Software", software_types, ruta)
otros = Fichero("Otros", None, ruta)