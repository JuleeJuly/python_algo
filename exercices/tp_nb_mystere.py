import random

nb_mystere = random.randint(1,100)
nb_essai = 5
gagne = 0
while nb_essai > 0 :
    try:
        saisie = int(input("Quel est le nombre mystere ? "))
        if 0 <= saisie <= 100 :
            if saisie == nb_mystere:
                gagne = 1
                break
            elif saisie < nb_mystere :
                print("trop petit")
                nb_essai = nb_essai -1
            elif saisie > nb_mystere :
                print("trop grand")
                nb_essai = nb_essai -1
        else :
            print("Ce n'est pas un nombre valide")
    except ValueError:
        print("Ce n'est pas un nombre valide")
if gagne == 1 :
    print("Felicitations !")
else:
    print("Vous avez atteint le nombre d'essai maximum, le nombre mystere était : ",nb_mystere)