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
