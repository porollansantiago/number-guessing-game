import unittest
from numbers import Guess
class Test_numbers(unittest.TestCase):
    def setUp(self):
        self.my_number = Guess('5678')
        self.guess = ['5678','1234','5432','5632','5673','6785','5555','7787','7717']
    def test_checkNumber_0(self):
        result = self.my_number.checkNumber(self.guess[0])
        self.assertEqual(result,'G: 4  |  R: 0')
    def test_checkNumber_1(self):
        result = self.my_number.checkNumber(self.guess[1])
        self.assertEqual(result,'G: 0  |  R: 0')
    def test_checkNumber_2(self):
        result = self.my_number.checkNumber(self.guess[2])
        self.assertEqual(result,'G: 1  |  R: 0')
    def test_checkNumber_3(self):
        result = self.my_number.checkNumber(self.guess[3])
        self.assertEqual(result,'G: 2  |  R: 0')
    def test_checkNumber_4(self):
        result = self.my_number.checkNumber(self.guess[4])
        self.assertEqual(result,'G: 3  |  R: 0')
    def test_checkNumber_5(self):
        result = self.my_number.checkNumber(self.guess[5])
        self.assertEqual(result,'G: 0  |  R: 4')
    def test_checkNumber_6(self):
        result = self.my_number.checkNumber(self.guess[6])
        self.assertEqual(result,'G: 1  |  R: 0')
    def test_checkNumber_7(self):
        result = self.my_number.checkNumber(self.guess[7])
        self.assertEqual(result,'G: 0  |  R: 2')
    def test_checkNumber_8(self):
        result = self.my_number.checkNumber(self.guess[8])
        self.assertEqual(result,'G: 0  |  R: 1')


if __name__ == '__main__':
    unittest.main()
