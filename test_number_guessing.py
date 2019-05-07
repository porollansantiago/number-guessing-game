from number_guessing import Number_guessing
import unittest

class Test_number_guessing(unittest.TestCase):
    def setUp(self):
        self.game = Number_guessing('9876')
        self.numbers = ('9876','9999','1234','8769','8976')

    def test_all_G(self):
        self.game.compare(self.numbers[0])
        result = self.game.get_result()
        self.assertEqual(result,'4G ')
    
    def test_repeated(self):
        self.game.compare(self.numbers[1])
        result = self.game.get_result()
        self.assertEqual(result, '1G ')
 
    def test_no(self):
        self.game.compare(self.numbers[2])
        result = self.game.get_result()
        self.assertEqual(result,'Sin coincidencias')
    
    def test_all_R(self):
        self.game.compare(self.numbers[3])
        result = self.game.get_result()
        self.assertEqual(result, '4R')

    def test_case1(self):
        self.game.compare(self.numbers[4])
        result = self.game.get_result()
        self.assertEqual(result,'2G 2R')   

if __name__ == '__main__':
    unittest.main()