import unittest
from pc import Numbers

class Test_PC(unittest.TestCase):
    def setUp(self):
        self.num = Numbers('9876')

    def test_A(self):
        tries = self.num.getTries()
        self.assertLess(tries,37)

    def test_Play(self):
        self.num.play()
        result = self.num.getFinalChoice()
        self.assertEqual(result,'9876')

if __name__ == '__main__':
    unittest.main()