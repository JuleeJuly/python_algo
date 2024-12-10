def compter_lettre_a(chaine : str):
    nb = 0
    for lettre in chaine:
        if lettre == "a" :
            nb = nb + 1
    return nb

def compter_lettre_b(chaine :str):
    nb = chaine.count("a")
    return nb

mot = str(input("Donner moi un mot : "))
print(compter_lettre_a(mot))
print(compter_lettre_b(mot))