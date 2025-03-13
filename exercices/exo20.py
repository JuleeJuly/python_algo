def verification_adn(chaine_adn: str):
    longueur = len(chaine_adn)
    erreur = True
    presence_a = 0
    presence_t = 0
    presence_c = 0
    presence_g = 0
    ok = False
    if longueur%4 != 0:
        erreur = False
    for lettre in chaine_adn:
        if lettre != "a" and lettre != "t" and lettre != "c" and lettre != "g" :
            erreur = False
        if lettre == "a":
            presence_a = 1
        if lettre == "t":
            presence_t = 1
        if lettre == "c":
            presence_c = 1
        if lettre == "g":
            presence_g = 1
    if presence_a == 1 and presence_c == 1 and presence_t == 1 and presence_g == 1:
        ok = True
    if ok == True and erreur == True:
        return erreur
    else:
        return False

def saisie_adn(texte :str):
    chaine_adn = str(input("Donnez moi une "+texte+" adn : "))
    resultat = verification_adn(chaine_adn)
    while resultat == False:
        chaine_adn = str(input("Donnez moi une "+texte+" adn : "))
        resultat = verification_adn(chaine_adn)
    return chaine_adn
        
def proportion(chaine_adn : str, sequence_adn : str):
    resultat = chaine_adn.count(sequence_adn)
    return resultat


chaine = saisie_adn("chaine")
sequence = saisie_adn("sequence")
print(proportion(chaine,sequence))
