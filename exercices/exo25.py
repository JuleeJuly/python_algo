liste_nombre = []
def ajout(liste: list):
    nb_nombre = 0
    while nb_nombre < 2:
        nbr = int(input("Ajouter un nombre : "))
        liste.append(nbr)
        nb_nombre = nb_nombre+1
    return liste
def affiche_liste(liste : list):
    for i in liste:
        print(i)

def affiche_resultat(nb1: int, nb2:int):
    mon_tuple = ("Somme = "+str(nb1+nb2),"Différence = "+str(nb1-nb2),"Quotient = "+str(nb1/nb2),"Produit = "+str(nb1*nb2))
    return mon_tuple

ajout(liste_nombre)
# affiche_liste(liste_nombre)
print(affiche_resultat(liste_nombre[0],liste_nombre[1]))