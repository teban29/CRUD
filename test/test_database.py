import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('11A','Juan','Perez'),
            db.Cliente('12B','Maria','Gomez'),
            db.Cliente('13C','Pedro','Garcia')
        ]