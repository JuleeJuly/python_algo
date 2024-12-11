liste_adresse = []
def affichage_menu():
    print("== MENU PRINCIPAL ==")
    print("1. Voir les adresses")
    print("2. Ajouter une adresse")
    print("3. Editer une adresse")
    print("4. Supprimer une adresse")
    print("0. Quitter le programme")
    choix_menu()

def choix_menu():
    choix = int(input("Votre choix : "))
    match choix:
        case 0:
            exit()
        case 1:
            voir_adresse()
            affichage_menu()
        case 2:
            ajouter_adresse()
            affichage_menu()
        case 3:
            editer_adresse()
            affichage_menu()
        case 4:
            supprimer_adresse()
            affichage_menu()
        case _:
            exit()

def voir_adresse():
    global liste_adresse
    print("== VOIR LES ADRESSES ==")
    for i in liste_adresse:
        print("Adresse n°",liste_adresse.index(i)," ",i["numero"]," ",i["complement"]," ",i["intitule"]," ",i["commune"]," ",i["cp"])
        # for key,value in i.items():
        #     print("clé : ",key," valeur : ",value)
def ajouter_adresse():
    global liste_adresse
    adresse = {}
    print("== AJOUTER UNE ADRESSE ==")
    adresse["numero"] = input("Veuillez entrer le numéro de voie SVP : ")
    adresse["complement"] = input("Veuillez entrer le complément d'adresse SVP : ")
    adresse["intitule"] = input("Veuillez entrer l'intitulé de voie SVP : ")
    adresse["commune"] = input("Veuillez entrer la commune SVP : ")
    adresse["cp"] = input("Veuillez entrer le code postal SVP : ")
    liste_adresse.append(adresse)
    print("L'adresse est ajouté ! ")
def editer_adresse():
    print("== EDITER ADRESSE ==")
    voir_adresse()
    presence = 0
    while presence == 0:
        if len(liste_adresse) == 0:
            print("Il n'y a pas d'adresse ! ")
            break
        nb = int(input("Quelle adresse voulez vous éditer ? : "))
        for i in liste_adresse:
            if nb == liste_adresse.index(i):
                presence = 1
                modifier_element(liste_adresse.index(i))
                # edition adresse , quel element voulez vous modifier ? 
                print("L'adresse est édité ! ")


def modifier_element(i : int):
    print("1. numéro")
    print("2. complément")
    print("3. intitulé")
    print("4. commune")
    print("5. CP")
    nb = int(input("Quelle élément voulez vous modifier ? : "))    
    match nb:
        case 1:
            liste_adresse[i]["numero"] = input("Veuillez entrer le numéro de voie SVP : ")
        case 2:
            liste_adresse[i]["complement"] = input("Veuillez entrer le complément d'adresse SVP : ")
        case 3:
            liste_adresse[i]["intitule"] = input("Veuillez entrer l'intitulé de voie SVP : ")
        case 4:
            liste_adresse[i]["commune"] = input("Veuillez entrer la commune SVP : ")
        case 5:
            liste_adresse[i]["cp"] = input("Veuillez entrer le code postal SVP : ")
        case _:
            exit()
def supprimer_adresse():
    print("== SUPPRIMER ADRESSE ==")
    voir_adresse()
    presence = 0
    while presence == 0:
        if len(liste_adresse) == 0:
            print("Il n'y a pas d'adresse ! ")
            break
        nb = int(input("Quelle adresse voulez vous supprimer ? : "))
        for i in liste_adresse:
            if nb == liste_adresse.index(i):
                presence = 1
                liste_adresse.pop(nb)
                print("L'adresse est supprimé ! ")
affichage_menu()