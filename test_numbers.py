import unittest
from numbers import Guess_number
class Test_numbers(unittest.TestCase):
    def setUp(self):
        self.my_number = Guess_number('5678')
        self.guess = ['5678','1234','5432','5632','5673','6785']
    def test_checkNumber_0(self):
        result = self.my_number.check_number(self.guess[0])
        self.assertEqual(result,'G: 4  |  R: 0')
    def test_checkNumber_1(self):
        result = self.my_number.check_number(self.guess[1])
        self.assertEqual(result,'G: 0  |  R: 0')
    def test_checkNumber_2(self):
        result = self.my_number.check_number(self.guess[2])
        self.assertEqual(result,'G: 1  |  R: 0')
    def test_checkNumber_3(self):
        result = self.my_number.check_number(self.guess[3])
        self.assertEqual(result,'G: 2  |  R: 0')
    def test_checkNumber_4(self):
        result = self.my_number.check_number(self.guess[4])
        self.assertEqual(result,'G: 3  |  R: 0')
    def test_checkNumber_5(self):
        result = self.my_number.check_number(self.guess[5])
        self.assertEqual(result,'G: 0  |  R: 4')


if __name__ == '__main__':
    unittest.main()
