while True:
    try:
        copie = int(input("Saisir un nombre de copie "))
        if copie < 10 :
            print("prix : " ,copie*0.5)
        elif copie >=10 and copie <= 20 :
            print("prix : " ,copie*0.4)
        elif copie > 20 :
            print("prix : " ,copie*0.3)
        break
    except ValueError:
        print("ce n'est pas un nombre, veuillez réessayer : ")

        