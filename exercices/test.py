import random
mon_tableau = [1,2,3,4,5,6,7,8,9]

random = random.randint(0,len(mon_tableau)-1)
try:
    nb = int(input("veuillez saisir un chiffre entre 1 et 9 ")) 
    if nb == random :
        print("Gagné !")
    else :
        while nb != random :
            nb = int(input("veuillez saisir un chiffre entre 1 et 9 "))  
    print("Gagné !")   
except ValueError:
    print("ce n'est pas un nombre, veuillez réessayer : ")
