# Dictionary = {1: "Hello World!"}

n = input("Ievadiet vārdu: ")
simboli = {}
for simbols in n:
    simboli[simbols] = 1

unikalie_simboli = len(simboli)
print("Unikālie simbolu skaits: ", unikalie_simboli)
