# tableau = []
# for x in range(6):
#     nbr = int(input("saisir un chiffre : "))
#     tableau.append(nbr)
# tableau.sort()
# print(tableau)

le_plus_grand = 0
for x in range(6):
    nbr = int(input("saisir un chiffre : "))
    if nbr > le_plus_grand :
        le_plus_grand = nbr
print(le_plus_grand)