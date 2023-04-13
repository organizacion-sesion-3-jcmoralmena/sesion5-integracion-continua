import unittest
import sys
 
# setting path
sys.path.append('..')


from funciones import es_par

class TestPar(unittest.TestCase):

    def test_par(self):
        self.assertTrue(es_par(2))
        
    def test_par2(self):
        self.assertTrue(es_par(2*2))
        
    def test_impar(self):
        self.assertFalse(es_par(5))
        
    def test_impar2(self):
        self.assertFalse(es_par(5*5))
        
