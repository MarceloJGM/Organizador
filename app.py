from tkinter import *
from tkinter import ttk
import os
import shutil
import sys

path = r'/home/marcelo/Descargas/'
path_2 = '/home/marcelo/'
ext_texto = ['.docx', '.txt', '.doc', '.pdf', '.pptx', '.jnt', '.pub', '.xlsx']
ext_foto = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
ext_video = ['.mov', '.mp4', '.avi', '.mkv']
ext_sfk = ['.sfk', '.exe', '.msi', '.rar', '.zip']


def Buscar_arch():
    return [arch.name for arch in os.scandir(path) if arch.is_file()]


def Ordenar():
    for archivo in Buscar_arch():
        try:
            nombre_archivo, ext = os.path.splitext(archivo)
            for i in ext_texto:
                if ext == i:
                    if os.path.exists(path_2 + 'Documentos/'):
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Documentos/')
                    else:
                        os.makedirs(path_2 + 'Documentos/')
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Documentos/')
            for i in ext_foto:
                if ext == i:
                    if os.path.exists(path_2 + 'Imágenes/'):
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Imágenes/')
                    else:
                        os.makedirs(path_2 + 'Imágenes/')
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Imágenes/')
            for i in ext_video:
                if ext == i:
                    if os.path.exists(path_2 + 'Vídeos/'):
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Vídeos/')
                    else:
                        os.makedirs(path_2 + '/Vídeos')
                        shutil.move(path + '/' + archivo,
                                    '/home/marcelo/Vídeos/')
            for i in ext_sfk:
                if ext == i:
                    if os.path.exists(path):
                        shutil.move(path + archivo,
                                    '/home/marcelo')
                    else:
                        os.makedirs(path)
                        shutil.move(path + archivo,
                                    '/home/marcelo/')

            print(f"El archivo '{archivo}' se ordenó correctamente.")

        except:
            print(f"El archivo '{archivo}' no se ha podido mover.")

if __name__ == "__main__":
    Buscar'arch()
    Ordenar()
