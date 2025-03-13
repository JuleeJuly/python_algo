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
nb = input("Saisi un chiffre ")
print(nb)

print(type(nb))

# cast de varible
nb_a = int(nb)
print(type(nb))

nb_b = int(input("Saisi un chiffre "))

print(f"Le nombre a est de : {nb_a} et le nombre b est de : {nb_b}")

print(f"{nb_a:^7.2f}")



une_var = 2
une_autre_var = 12
print(une_var*une_autre_var)
if une_autre_var<une_var :
    print("la supériorité ")
    
else :
    print("ok")
var_enc = 2*une_var
print(var_enc)
