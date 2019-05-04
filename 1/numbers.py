import random
class Guess_number:
    def __init__(self,to_guess = random.randint(1000,9999)):
        self.to_guess = str(to_guess)
        self.g = 0
        self.r = 0
    def check_number(self,number):
        self.g = 0
        self.r = 0
        try:
            int(number)
            for idx, digit in enumerate(number):
                if digit == self.to_guess[idx]:
                    self.g += 1
                elif digit in self.to_guess:
                    self.r += 1
        except IndexError:
            return "El numero debe ser de cuatro digitos"
        except ValueError:
            return "No pueden ingresarse letras"
        else:
            result = 'G: ' + str(self.g) + "  |  R: " + str(self.r)
            return result
    
    def check_win(self):
        if self.g == 4:
            print("Ha adivinado el numero")
            return False
        return True