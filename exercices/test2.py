import random
mon_tableau = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5"]
ma_liste = random.sample(mon_tableau,5)
try:
    a = 5
    while a !=0 :
        lettre = str(input("veuillez saisir une lettre A/B/C/D "))
        nb = str(input("veuillez saisir un chiffre entre 1 et 5 ")) 
        for x in ma_liste:
            if lettre+nb == x :
                print("Gagné !")
                a = a-1 
                ma_liste.remove(x)
except ValueError:
    print("ce n'est pas un nombre, veuillez réessayer : ")