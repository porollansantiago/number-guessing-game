from numbers import Guess
import random
class Numbers:
    def __init__(self):
        self.guess = '0000'
        self.result = ''            
        self.number = Guess('1234')
        self.tries = 0

    def getResult(self):
        self.result = self.number.checkNumber(self.guess)
        self.result = self.result[3] + self.result [12]
        return self.result

    def play(self):
        self.guess = str(random.randint(1000,9999))
        self.tries += 1
    
    def getTries(self):
        return self.tries

num = Numbers()
while num.number.checkWin():
    print(num.getResult())
    num.play()
print(num.getTries())