import copy
import unittest
import database as db

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
        self.assertIsNone(cliente_rebuscado)