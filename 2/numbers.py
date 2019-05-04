import random
class Guess:
    def __init__(self,number = random.randint(1000,9999)):
        self.number = str(number)
        self.g = 0
        self.r = 0
        self.result = ''
    def checkNumber(self,guess):
        self.g = 0
        self.r = 0
        for idx, letter in enumerate(guess):
            if self.number[idx] == letter:
                self.g += 1
        for idx, letter in enumerate(self.number):
            if guess[idx] in self.number and guess[idx] != letter :
                self.r += 1
        self.result = self.g,'G  ',self.r,'R'
        return self.result
    def checkWin(self):
        if self.g == 4:
            return False
        return True

def runGame ():
    my_number = Guess(1234)
    game = True
    while game:
        guess = input("Adivina el numero: ")

        print(my_number.checkNumber(guess))
        game = my_number.checkWin()

runGame()