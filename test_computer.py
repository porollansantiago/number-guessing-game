from computer import Computer
import unittest

class Test_computer(unittest.TestCase):
    def setUp(self):
        self.computer = Computer('9999')
        self.computer.play()

    def test_tries(self):
        tries = self.computer.game.get_tries()
        self.assertLess(tries,37)
    
    def test_number(self):
        number = self.computer.getNumber()
        self.assertEqual(number,'9999')

if __name__ == '__main__':
    unittest.main()

