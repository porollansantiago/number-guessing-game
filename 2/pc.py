from numbers import Guess
import random
class Numbers:
    def __init__(self,randomNumber = random.randint(1000,9999)):
        self.guess = '0000'
        self.result = ''            
        self.number = Guess(str(randomNumber))
        self.tries = 0

    def getResult(self,x):
        self.result = self.number.checkNumber(x)
        self.result = self.result[3] + self.result [12]
        return self.result

    def play(self):
        self.getResult(self.guess)

        for idx, value in enumerate(self.guess):
            while True:
                self.tries += 1
                x = ''
                prevResult = self.result
                self.guess = list(self.guess)
                self.guess[idx] = str(int(self.guess[idx]) + 1)
                x = ''.join(self.guess)
                self.getResult(x)
                if int(self.result[0]) > int(prevResult[0]):
                    break

                if int(self.result[0]) < int(prevResult[0]):
                    self.guess[idx] = str(int(self.guess[idx]) -1)
                    break
                self.guess = ''.join(self.guess)


    def getTries(self):
        return self.tries
    def getFinalChoice(self):
        x = ''.join(self.guess)
        return x