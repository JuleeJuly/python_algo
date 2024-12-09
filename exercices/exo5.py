while True:
    try:
        age = int(input("Saisir un nombre "))
        if (age%3) == 0:
            print("le nombre est divisible par 3")
        else:
            print("le nombre n'est pas divisible par 3")
        break
    except ValueError:
        print("ce n'est pas un nombre, veuillez réessayer : ")

        
