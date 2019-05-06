from number_guessing import Number_guessing

def main():
    game = Number_guessing()

    while game.check_win():
        number = input("Adivine: ")
        print(game.compare(number))

    print("Se ha terminado en ",game.get_tries()," intentos")

main()

