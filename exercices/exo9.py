age = int(input("Saisir l'age "))
salaire = int(input("Saisir le salaire "))
exp = int(input("Saisir l'experience "))
ok = 0

if age < 30 :
    print("l'age n'est pas respecté")
else :
    ok = ok+1
if salaire > 40000 :
    print("le salaire est trop haut")
else :
    ok = ok+1
if exp < 5 :
    print("l'experience n'est pas assez longue")
else :
    ok = ok+1
if ok == 3 :
    print("Vous êtes embauché !")
