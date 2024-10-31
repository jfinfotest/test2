import unittest
import assessment  # Asegúrate de que assessment.py exista y sea importable

class TestAssessment(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(assessment.suma(2, 2), 4)
        self.assertEqual(assessment.suma(-1, 1), 0)
        self.assertEqual(assessment.suma(10, 5), 15)

    def test_resta(self):
        self.assertEqual(assessment.resta(5, 3), 2)
        self.assertEqual(assessment.resta(10, 2), 8)
        self.assertEqual(assessment.resta(-5, 2), -7)

# Esto es crucial para que unittest funcione.  De lo contrario, no se ejecutará nada.
if __name__ == '__main__':
    unittest.main()
