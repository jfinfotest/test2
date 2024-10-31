import unittest

class TestAssessment(unittest.TestCase):
            def test_suma(self):
                self.assertEqual(namespace['suma'](2, 2), 4)
                self.assertEqual(namespace['suma'](-1, 1), 0)
                self.assertEqual(namespace['suma'](10, 5), 15)

            def test_resta(self):
                self.assertEqual(namespace['resta'](5, 3), 2)
                self.assertEqual(namespace['resta'](10, 2), 8)
                self.assertEqual(namespace['resta'](-5, 2), -7)
