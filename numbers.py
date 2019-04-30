class guess_number:
    def __init__(self,to_guess='1234'):
        self.to_guess = str(to_guess)
        self.g = 0
        self.r = 0
    def check_number(self,number):
        self.g = 0
        self.r = 0
        for idx, digit in enumerate(number):
            if digit == self.to_guess[idx]:
                self.g += 1
            elif digit in self.to_guess:
                self.r += 1
        
        print("G: ", self.g)
        print("R: ", self.r)


my_number = guess_number('5432')
while True:
    number = input("adivine el numero: ")
    my_number.check_number(number)


