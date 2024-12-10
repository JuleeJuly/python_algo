temp = int(input("Saisir la température : "))
if temp < 0 :
    print("SOLIDE")
elif  0 <= temp <= 100:
    print("LIQUIDE")
elif temp > 100:
    print("GAZEUX")