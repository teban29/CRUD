import copy
import unittest
import database as db
import helpers
import config
import csv

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('11A','Juan','Perez'),
            db.Cliente('12B','Maria','Gomez'),
            db.Cliente('13C','Pedro','Garcia')
        ]
        
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('11A')
        cliente_ineexistente = db.Clientes.buscar('14D')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_ineexistente)
        
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('14D','Carlos','Lopez')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevo_cliente.dni,'14D')
        self.assertEqual(nuevo_cliente.nombre,'Carlos')
        self.assertEqual(nuevo_cliente.apellido,'Lopez')
        
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('11A'))
        cliente_modificado = db.Clientes.modificar('11A','Carlos','Perez')
        self.assertEqual(cliente_a_modificar.nombre,'Juan')
        self.assertEqual(cliente_modificado.nombre,'Carlos')
        
    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('11A')
        cliente_rebuscado = db.Clientes.buscar('11A')
        self.assertEqual(cliente_borrado.dni, '11A')
        
    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A',db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('113213', db.Clientes.lista))
        
    def test_escritura_csv(self):
        db.Clientes.borrar('11A')
        db.Clientes.borrar('12B')
        db.Clientes.modificar('13C', 'Ayrton', 'Senna')
        
        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            dni, nombre, apellido = next(reader)
            
        self.assertEqual(dni, '13C')
        self.assertEqual(nombre, 'Ayrton')
        self.assertEqual(apellido, 'Senna')
        
        