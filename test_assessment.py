import unittest

class TestAssessment(unittest.TestCase):
    """
    Clase de pruebas para evaluar las funciones del assessment
    """
    
    def test_suma(self):
        """Prueba la función suma con diferentes casos"""
        self.assertEqual(suma(2, 2), 4, "La suma de 2 + 2 debe ser 4")
        self.assertEqual(suma(-1, 1), 0, "La suma de -1 + 1 debe ser 0")
        self.assertEqual(suma(10, 5), 15, "La suma de 10 + 5 debe ser 15")
        self.assertEqual(suma(0, 0), 0, "La suma de 0 + 0 debe ser 0")
        self.assertEqual(suma(-5, -3), -8, "La suma de -5 + -3 debe ser -8")

    def test_resta(self):
        """Prueba la función resta con diferentes casos"""
        self.assertEqual(resta(5, 3), 2, "La resta de 5 - 3 debe ser 2")
        self.assertEqual(resta(10, 2), 8, "La resta de 10 - 2 debe ser 8")
        self.assertEqual(resta(-5, 2), -7, "La resta de -5 - 2 debe ser -7")
        self.assertEqual(resta(0, 0), 0, "La resta de 0 - 0 debe ser 0")
        self.assertEqual(resta(3, 5), -2, "La resta de 3 - 5 debe ser -2")

if __name__ == '__main__':
    unittest.main()
