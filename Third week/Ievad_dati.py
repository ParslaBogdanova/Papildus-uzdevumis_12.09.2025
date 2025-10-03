# 1.uzdevums:
import math

C = float(input("Temperatūru Celsija grādos: "))
if C <= -273.15:
    print("Temperatūra zem absolūtās nulles fiziksi nav iespējama.")
F = (C * (9/5)) + 32
K = C + 273.15

if K < 0:
    print("Temperatūra zem absolūtās nulles fiziksi nav iespējama.")
elif F > 212:
    print("Temperatūra ir virs ūdens viršnas temperatūra")
elif F < 32:
    print("Temperatūra ir zem ūdens sasalšanas punkta")
else:
    print("Temperatūra ir starp ūdens sasalšanas un viršanas temperatūru.")
print(C, F, K)

# 2.uzdevums:
Gaismas_atrums = 299_791_485
while True:
    m = int(input("Ievadiet gaismas ātrumu: "))

    if m > Gaismas_atrums:
        print("Pārāk liels skaitlis!")
    elif m < Gaismas_atrums:
        print("Pārāk mazs skaitlis!")
    else:
        print("Pareizi! Gaismas ātrums ir 299'791'485 m/s")
        break

# 3.Uzdevums
parole = "E=mc^2"
attempts = 0
max_attempts = 3

while True:
    liet_parol = input("Ievadiet paroli, lai piekļūtu fiikas laboratorijai: ")

    if parole != liet_parol:
        attempts += 1
        print("Nepareiza parole, mēģiniet vēlreiz!")
        if attempts == max_attempts:
            print("Pārāk daudz nepareizu mēģinājumu, piekļuve liegta.")
    else:
        print("Piekļūve piešķirta")
        break

# 4.uzdevums
saraksts = ["F=ma", "E=mc^2", "V=IR", "P=IV", "K.E. = 1/2 mv^2"]
for lists in saraksts:
    print(lists)
    if "E=mc^2" == lists:
        break

# 5 uzdevums
ievad_dati = [0, 1, 2, 3]
rindu_sk = len(ievad_dati)
kolonu_sk = len(ievad_dati)

for i in range(rindu_sk):
    for j in range(kolonu_sk):
        if i == j
        print(ievad_dati[i], end=" ")
        else:
            print(0, end=" ")
            print(" ")
