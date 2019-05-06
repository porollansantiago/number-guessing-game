from computer import Computer

def main():
    to_guess = input("Numero a adivinar: ")
    computer = Computer(to_guess)
    while computer.game.check_win():
        computer.play()
    print("\nNumero adivinado por la computadora: ",computer.getNumber())
    print("Se ha terminado en ",computer.game.get_tries()," intentos")

main()