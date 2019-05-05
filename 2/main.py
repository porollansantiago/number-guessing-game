from pc import Numbers

def main():
    randomNumber = input("Numero a adivinar: ")
    num = Numbers(randomNumber)
    num.play()
    print("Se ha adivinado el numero en ",num.getTries()," intentos")

main()


