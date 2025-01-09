import os 
import platform
import re

def limpiar_pantalla():
    os.system('cls' if platform.system() == 'Windows' else os.system('clear'))
    
def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    if mensaje:
        print(mensaje)
    while True:
        texto = input("> ").strip()
        if longitud_min <= len(texto) <= longitud_max:
            return texto
        print(f"Error: el texto debe tener entre {longitud_min} y {longitud_max} caracteres.")

def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$',dni):
        print("DNI incorrecto, debe cumplir el formato 00A")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI ya existente")
            return False
    return True