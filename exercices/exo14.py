population_initiale = int(input("saisir la population initiale : "))
taux = float(input("saisir le taux d'accroissement : "))
population_visee = int(input("saisir la population visée: "))
i = 1
resultat = population_initiale*(1+taux)
while resultat < population_visee:
    resultat = resultat *(1+taux)
    i = i+1
print(i)