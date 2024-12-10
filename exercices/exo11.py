capital = 10000
taux = 0.04
i = 1
resultat = capital*(1+taux)
print(resultat)
while resultat < capital*2:
    resultat = resultat *(1+taux)
    i = i+1
print(i)