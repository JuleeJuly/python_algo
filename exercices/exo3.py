from math import *
rayon = float(input("Saisir un rayon : "))
hauteur = float(input("Saisir une hauteur : "))
volume = round(((pi*(rayon**2)*hauteur)/3),2)
print("Le volume est de : ",volume," arrondi à deux chiffres")