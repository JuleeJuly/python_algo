import random
# TABLEAU DES POSSIBILITES
possibilites = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
# TABLEAU DE TEST DE L'IA
tableau_de_test = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
# tableau de l'utilisateur
cases_utilisateur = []
# l'adversaire choisi ses cases
cases_adversaire = random.sample(possibilites,5)
# l'utilisateur peut choisir 5 cases
for i in range(5) :
    # tant que p != 1 , alors l'utilisateur devra saisir une combinaison correct
    p = 0
    while p == 0 :
        # l'utilisateur choisi ses cases
        case = str(input("veuillez saisir une combinaison de A-E et de 1-5 (exemple : B4) : ")).upper()
        # on verifie que c'est une combinaison possible
        for pos in possibilites :
            # si la combinaison est possible, on l'ajoute dans son tableau de cases
            if case == pos :
                # on verifie que la case n'est pas deja ajouté
                v = 0
                for pos_ut in cases_utilisateur :
                    if case == pos_ut:
                       print("Vous avez déjà ajouté cette case ! ") 
                       v = 1
                if v == 0 :
                    cases_utilisateur.append(case)
                    p = 1
        if p == 0 :
            print("Vous devez saisir une combinaison correct ! ")
while ( not len(cases_adversaire) == 0 and not len(cases_utilisateur) == 0) :
    # l'adversaire choisi une case
    case_choisi = random.sample(tableau_de_test,1)
    t = 0
    for x in cases_utilisateur :
        for c in case_choisi :
            if c == x :
                cases_utilisateur.remove(c)
                print("L'adversaire a trouvé la case : ",c)
                t = 1
                if len(cases_utilisateur) == 0 :
                    print("L'adversaire a gagné")
                    break
    if t == 0 :
        print("L'adversaire s'est trompé",case_choisi)
        tableau_de_test.remove(c)
    # l'utilisateur choisi une case
    case_choisi_utilisateur = str(input("veuillez saisir une combinaison de A-E et de 1-5 (exemple : B4) : ")).upper()
    for x in cases_adversaire :
        if case_choisi_utilisateur == x :
            cases_adversaire.remove(case_choisi_utilisateur)
            print("Vous avez trouvé la case : ",case_choisi_utilisateur)           
            t = 1
            if len(cases_adversaire) == 0 :
                    print("Vous avez gagné")
                    break
    if t == 0 :
        print("Vous vous êtes trompé")