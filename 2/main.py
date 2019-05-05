from pc import Numbers

def main():
    randomNumber = input("Numero a adivinar: ")
    num = Numbers(randomNumber)
    num.play()
    print("Adivina: ",num.getFinalChoice()," en ",num.getTries()," intentos")

main()


