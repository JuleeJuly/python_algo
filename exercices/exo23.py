ma_liste = []
nb_note = int(input("Combien de note à rentrer ? Si 0, une note négative stoppera la saisie : "))
if nb_note > 0 :
    for i in range(nb_note):
        note = float(input("Saisir une note : "))
        ma_liste.append(note)
elif nb_note == 0:
    note = float(input("Saisir une note : "))
    
    if note >= 0:
        ma_liste.append(note)
    while note >= 0:
        note = float(input("Saisir une note : "))
        if note >= 0:
            ma_liste.append(note)
            nb_note = nb_note+1

ma_liste.sort()
total = 0
for elem in ma_liste:
    total = total+elem
moyenne = total/nb_note
print("Note min : ",ma_liste[0])
print("Note max : ",ma_liste[nb_note-1])
print("Note moyenne : ",moyenne)