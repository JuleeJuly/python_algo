liste_adresse = []
def affichage_menu():
    print("== MENU PRINCIPAL ==")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimer une adresse")
    print("0. Quitter le programme")

def choix_menu():
    choix = int(input("Votre choix : "))
    match choix:
        case 0:
            return False
        case 1:
            voir_adresse()
        case 2:
            ajouter_adresse()
        case 3:
            editer_adresse()
        case 4:
            supprimer_adresse()
        case _:
            return False

def voir_adresse()
def ajouter_adresse()
def editer_adresse()
def supprimer_adresse()
    

    
affichage_menu()
choix_menu()
