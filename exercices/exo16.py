def nom_prenom(nom : str,prenom : str) :
    return prenom.capitalize()+" "+nom.capitalize()

nom = str(input("Votre nom :  "))
prenom = str(input("Votre prenom :  "))
print(nom_prenom(nom,prenom))