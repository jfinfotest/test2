import unittest
import assessment

class TestAssessment(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(assessment.suma(2, 3), 5)
        self.assertEqual(assessment.suma(-1, 1), 0)

    def test_resta(self):
        self.assertEqual(assessment.resta(5, 2), 3)
        self.assertEqual(assessment.resta(1, -1), 2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2) # Importante: exit=False