from numbers import Guess

my_number = Guess()
game = True
while game:
        guess = input("Adivina: ")
        print(my_number.checkNumber(guess))
        game = my_number.checkWin()

if not game:
	print("Se ha adivinado el numero en ",my_number.getTries()," intentos")

