#Funciones

import os
import shutil
from variables import doc_types, img_types, software_types, carpetas

def crear_carpetas(ruta_base):
    for carpeta in carpetas:
        os.makedirs(os.path.join(ruta_base, carpeta), exist_ok=True)

def mover_archivos(ruta_base):
        
       for archivo in os.listdir(ruta_base):
            if os.path.isdir(os.path.join(ruta_base, archivo)):
                continue
            ext = os.path.splitext(archivo)[1]
            ext = ext.lower()

            if ext in img_types:
                destino = 'Imagenes'    
            elif ext in doc_types:
                destino = 'Documentos'
            elif ext in software_types:
                destino = 'Software'
            else:
                destino ='Otros'

            shutil.move(
                os.path.join(ruta_base, archivo),
                os.path.join(ruta_base, destino, archivo)
            )
            
def organizar_descargas(ruta_base):
    crear_carpetas(ruta_base)
    mover_archivos(ruta_base)