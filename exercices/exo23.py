ma_liste = []
nb_note = 0

# calcul de la moyenne
def moyenne(liste : list):
    total = 0
    for elem in ma_liste:
        total = total+elem
    moyenne = total/nb_note
    return moyenne
# trie de la liste
def tri_liste(ma_liste : list):
    ma_liste.sort()
    return ma_liste
# affichage moyenne
def affiche_moyenne(ma_liste : list):
    print("Note moyenne : ",moyenne(ma_liste))
# affichage max
def affiche_max(ma_liste : list,nb_note : int):
    print("Note max : ",ma_liste[nb_note-1])
# affichage min
def affiche_min(ma_liste : list):
    print("Note min : ",ma_liste[0])
# saisie des notes
def saisir_note():
    note = float(input("Saisir une note : "))
    while note > 20 :
        note = float(input("Note incorrect, recommence : "))
    return note
# fonction saisie de la liste des notes
def saisir_liste_note():
    global ma_liste
    global nb_note
    nb_note = int(input("Combien de note à rentrer ? Si 0, une note négative stoppera la saisie : "))
    while nb_note < 0 :
        print("erreur, recommence")
        nb_note = int(input("Combien de note à rentrer ? Si 0, une note négative stoppera la saisie : "))
    if nb_note > 0 :
        for i in range(nb_note):
            note = saisir_note()
            while note < 0:
                 print("erreur, recommence")
                 note = saisir_note()
            ma_liste.append(note)
    elif nb_note == 0:
        note = saisir_note()
        if note >= 0:
            ma_liste.append(note)
            nb_note = nb_note+1 
            while note >= 0:
                note = saisir_note()
                if note >= 0:
                    ma_liste.append(note)
                    nb_note = nb_note+1 


# execution
saisir_liste_note()
if len(ma_liste) > 0:
    tri_liste(ma_liste)
    affiche_min(ma_liste)
    affiche_max(ma_liste,nb_note)
    affiche_moyenne(ma_liste)
else :
    print("Vous n'avez rentré aucune note !")