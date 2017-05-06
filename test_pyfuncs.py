#test_pyfuncs

import unittest

from pyfuncs import Hamming

class test_Hamming(unittest.TestCase):

    def test_1(self):
        self.assertEqual(Hamming('1','1'),0)

    def test_10(self):
        self.assertEqual(Hamming('1','0'),1)

    def test_2(self):
        self.assertEqual(Hamming('10','01'),2)   

    def test_3(self):
        self.assertEqual(Hamming('10','11'),1)

    def test_5(self):
        self.assertEqual(Hamming('10101','11111'),2)
  

if __name__ =='__main__':
    unittest.main()
