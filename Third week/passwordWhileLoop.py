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
