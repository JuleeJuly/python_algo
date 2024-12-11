import random
# liste_concurrent = ["Olson Derrick","Newton Emylia","Thompson Jéthro", "Sanchez Carlos","Daniels Bob","Morton Jimmy", "Barre Maël",  "Evans Lucas"]
liste_concurrent = []
# faire passer le premier en dernier
def panne_moteur(liste : list):
    premier = liste[0]
    liste.pop(0)
    liste.append(premier)
    return liste
# inverse le premier et le deuxieme
def passe_en_tete(liste : list):
    premier = liste[0]
    deuxieme = liste[1]
    liste.pop(0)
    liste.pop(0)
    liste.insert(0,premier)
    liste.insert(0,deuxieme)
    return liste
# inverse l'avant dernier et le dernier
def sauve_honneur(liste : list):
    nb_element = recup_nombre_element(liste)
    dernier = liste[nb_element-1]
    avant_dernier = liste[nb_element-2]
    liste.pop(nb_element-1)
    liste.pop(nb_element-2)
    liste.append(dernier)
    liste.append(avant_dernier)
    return liste
# supprimer le premier
def tir_blaster(liste : list):
    liste.pop(0)
    return liste
# ajoute un concurrent à la fin
def retour_innatendu(liste: list):
    liste.append( "Chuck Norris")
    return liste
# affiche la liste des concurrents
def affiche_liste(liste : list):
    for i in liste:
        print(i)
# calcul le nombre d'elements de la liste
def recup_nombre_element(liste: list):
    nb_element = 0
    for i in liste:
        nb_element = nb_element+1
    return nb_element
# ajout des concurrent
def ajout_concurrent(liste: list):
    nb_concurrent = 0
    while nb_concurrent < 4:
        nb_concurrent = int(input("Combien de concurrent voulez vous ajouter ? (minimum 4): "))
    for i in range(nb_concurrent):
        concurrent = str(input("Ajouter le nom du concurrent : "))
        liste.append(concurrent)
    return liste
# lancement de la course
def lancement_course(liste : list):
    random.shuffle(liste)
    return liste

liste_concurrent = ajout_concurrent(liste_concurrent)
print("*******LISTE CONCURRENT******")
print("-----------------------------")
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******LANCEMENT COURSE******")
print("-----------------------------")
liste_concurrent = lancement_course(liste_concurrent)
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******PANNE MOTEUR******")
print("-----------------------------")
liste_concurrent = panne_moteur(liste_concurrent)
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******PASSE EN TETE******")
print("-----------------------------")
liste_concurrent = passe_en_tete(liste_concurrent)
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******SAUVE HONNEUR******")
print("-----------------------------")
liste_concurrent = sauve_honneur(liste_concurrent)
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******TIR BLASTER******")
print("-----------------------------")
liste_concurrent = tir_blaster(liste_concurrent)
affiche_liste(liste_concurrent)
print("-----------------------------")
print("*******RETOUR INNATENDU******")
print("-----------------------------")
liste_concurrent = retour_innatendu(liste_concurrent)
affiche_liste(liste_concurrent)