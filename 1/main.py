from numbers import Guess_number

my_number = Guess_number()
game = True
while game:
        guess = input("guess: ")
        print(my_number.check_number(guess))
        game = my_number.check_win()

