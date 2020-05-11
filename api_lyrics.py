import json
from pathlib import Path
import requests
import os

def MenuPrincipal():
    while True:
        try:   
            os.system ("cls") 
            print("---LYRICS---")
            print("1. Mostrar la letra de Let it be de The Beatles.")
            print("2. Mostrar la letra de Lo que en silencio guardo de Kaze.")
            print("3. Introducir un artista, una cancion suya y se mostrará su letra.")
            print("4. Salir")
            opcion=int(input("Elige una opcion: "))

            if opcion==1:
                Beatles()
                input("Vuelva al menú principal pulsando cualquier tecla: ")
            elif opcion==2:
                Kaze()
                input("Vuelva al menú principal pulsando cualquier tecla: ")
            elif opcion==3:
                LetraGeneral()
                input("Vuelva al menú principal pulsando cualquier tecla: ")
            elif opcion==4:
                print("Finalizando programa.........")
                break
            else:
                opcion=input("Opción no válida, vuelva al menú principal pulsando cualquier tecla ")
        except:
            opcion=input("Tipo de dato no válido, vuelva al menú principal pulsando cualquier tecla ")


def Beatles():
    while True:
        try:
            api_address="https://api.lyrics.ovh/v1/The Beatles/Let it be"
            resp = requests.get(api_address)
            if resp.status_code==200:
                json_data=json.loads(resp.content)
                print(json_data)
            break    
        except:
            input("Tipo de dato no válido, vuelva al menú principal pulsando cualquier tecla ")

def Kaze():
    while True:
        try:
            api_address="https://api.lyrics.ovh/v1/Kaze/Lo que en silencio guardo"
            resp = requests.get(api_address)
            if resp.status_code==200:
                json_data=json.loads(resp.content)
                print(json_data)
            break    
        except:
            input("Tipo de dato no válido, vuelva al menú principal pulsando cualquier tecla ")

def LetraGeneral():
    while True:
        try:
            artista=input("Introduzca un artista: ")
            cancion=input("Introduzca una canción de dicho artista: ")
            api_address=("https://api.lyrics.ovh/v1/%s/%s" %(artista,cancion))
            resp = requests.get(api_address)
            if resp.status_code==200:
                json_data=json.loads(resp.content)
                print(json_data)
                break
            else:
                print("Has introducido los datos incorrectamente o bien no contamos con esa letra")
                
        except:
            input("Tipo de dato no válido, vuelva al menú principal pulsando cualquier tecla ")


MenuPrincipal()