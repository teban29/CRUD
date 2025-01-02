import os
import helpers


def iniciar():
    while True:
        helpers.limpiar_pantalla()
        
        print("================================")
        print("Bienvenido al sistema de gestión")
        print("================================")
        print("1. Listar clientes")
        print("2. Buscar un cliente")
        print("3. Crear un cliente")
        print("4. Modificar un cliente")
        print("5. Borrar un cliente")
        print("6. Salir")
        print("================================")
        
        opcion = input("> ")
        os.system('clear') #cls para windows
        
        if opcion == '1':
            print("Listado de clientes")
            print("===================")
            #TODO
        
        elif opcion == '2':
            print("Buscando cliente")
            print("=================")
            #TODO
        
        elif opcion == '3':
            print("Creando cliente")
            print("================")
            #TODO 
            
        elif opcion == '4':
            print("Modificando cliente")
            print("===================")
            #TODO
            
        elif opcion == '5':
            print("Borrando cliente")
            print("=================")
            #TODO
            
        elif opcion == '6':
            print("Saliendo")
            break
        
        input("Presione Enter para continuar...")
        