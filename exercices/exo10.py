# saisie = int(input("saisir un chiffre entre 1 et 3 : "))
# while (not saisie == 1 or not saisie == 2 or not saisie == 3) :
#     print("saisie",saisie)
#     saisie = int(input("saisir un chiffre entre 1 et 3 : "))
while True: 
    nbr = int(input("saisir un chiffre entre 1 et 3 : "))
    if 1 <= nbr <= 3:
        break
    else:
        print("erreur")