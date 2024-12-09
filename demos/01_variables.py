# print hello world ctrl :
print("Hello world")

print("------------")
print("Les variables")

ma_variable = 5

ma_variable_2 = 2 * ma_variable

# les types numériques
var = 23
var = 23.5
print(type(var))

#  le type chaine de caracteres

var = "ma chaine de caracteres"

print(type(var))

#  les bolleens
var = True
var = False

# Récupération d'une valeur par mun utilisateur
nb = input("Saisi un chiffre connard !")
print(nb)

print(type(nb))

# cast de varible
nb_a = int(nb)
print(type(nb))

nb_b = int(input("Saisi un chiffre connard ! "))

print(f"Le nombre a est de : {nb_a} et le nombre b est de : {nb_b}")

print(f"{nb_a:^7.2f}")



ta_mere = 2
ton_pere = 12
print(ta_mere*ton_pere)
if ton_pere<ta_mere :
    print("la supériorité mec ! ")
    
else :
    print("dtc")
ton_fils = 2*ta_mere
print(ton_fils)

ta_fille = 12.5

# match
#     case 1:
#         return "fuck you"
#     case 2:
#     case 3:
