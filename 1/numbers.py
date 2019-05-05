import random
class Guess:
    def __init__(self,number = random.randint(1000,9999)):
        self.number = str(number)
        self.g = 0
        self.r = 0
        self.r1 = {}
        self.result = ''
        self.tries = 0
    def checkNumber(self,guess):
        self.g = 0
        self.r = 0
        self.r1 = {}
        self.tries += 1
        try:
            int(guess)
            for idx, letter in enumerate(guess):
                if self.number[idx] == letter:
                    self.g += 1
                else:
                    if self.number[idx] in guess:
                        self.r1[letter] = 1
        except IndexError:
            return "El numero debe ser de cuatro digitos"
        except ValueError:
            return "Solo se pueden ingresar numeros"
        else:
            for value in self.r1:
                self.r = self.r + self.r1[value]
            self.result = 'G: ' + str(self.g) + '  |  R: ' + str(self.r)
            return self.result
    def checkWin(self):
        if self.g == 4:
            return False
        return True
    def getTries(self):
        return self.tries