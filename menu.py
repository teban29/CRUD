import os
import helpers
import database as db

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
        helpers.limpiar_pantalla()
        
        if opcion == '1':
            print("Listado de clientes")
            print("===================")
            for cliente in db.Clientes.lista:
                print(cliente)
        
        elif opcion == '2':
            print("Buscando cliente")
            print("=================")
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado")
        
        elif opcion == '3':
            print("Creando cliente")
            print("================")
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            nombre = helpers.leer_texto(3,30,"Nombre (3 a 30 caracteres)").capitalize()
            apellido = helpers.leer_texto(3,30,"Apellido (3 a 30 caracteres)").capitalize()
            db.Clientes.crear(dni,nombre,apellido)
            print("Cliente creado")
            
            
        elif opcion == '4':
            print("Modificando cliente")
            print("===================")
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(3,30,f"Nombre (3 a 30 caracteres) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(3,30,f"Apellido (3 a 30 caracteres) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre,apellido)
                print("Cliente modificado")
            else:
                print("Cliente no encontrado")
            
        elif opcion == '5':
            print("Borrando cliente")
            print("=================")
            dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
            db.Clientes.borrar(dni)
            print("Cliente borrado") if db.Clientes.borrar(dni) else print("Cliente no encontrado")
            
            
        elif opcion == '6':
            print("Saliendo")
            break
        
        input("Presione Enter para continuar...")
        