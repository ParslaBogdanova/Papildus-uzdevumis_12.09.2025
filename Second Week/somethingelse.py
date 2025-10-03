# a_str, b_str, c_str = input("Ievadi trīs skaitļus ").split()
# a, b, c = int(a_str), int(b_str), int(c_str)

# lists = [a, b, c]
# lists.sort()
# print(lists)

# Izveidot programmu, kas lietotājam prasa ievadīt skaitli decimālajā sistēmā un
# izdrukā šī skaitļa ciparu summu, piemēram,
# skaitļa 12793 ciparu summa ir 22=1+2+7+9+3.
# Programmas kodu ieraksti atbildes logā!


# skaitlis_input = int(input("Ievadiet sakitli decimālajā sistēmā: "))
# skaitlis_lists = list(map(int, str(skaitlis_input)))
# # summa = 0
# # for i in skaitlis_lists:
# #     summa += i
# summa = sum(skaitlis_lists)
# print(summa)

# input_s = int(input("Ievadiet skaitli decimālājā sistēmā: "))
# sum = 0
# for i in str(input_s):
#     sum += int(i)

# print(sum)


# # masa (10²⁴ kg) https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# katalogs = {"Merkurs": 0.330, "Venēra": 4.87, "Zeme": 5.97, "Marss": 0.642,
#             "Jupiters": 1898, "Saturns": 568, "Urāns": 86.8, "Neptūns": 102}

# for p in sorted(katalogs):
#     print(p, katalogs[p])


"""
Salīdzinoši populārajā galda spēlē “Šahs” figūras var atrasties uz lauciņiem,
kas izvietoti 8 rindās un 8 kolonās, veidojot kvadrāta formas galdiņu.
Rindas tiek secīgi numurētas ar skaitļiem no 1 līdz 8,
bet kolonas ar latīņu alfabēta pirmajiem burtiem no "a" līdz "h".
Parasti, attēlojot šaha galdiņu uz ekrāna, lauciņš "a1" atrodas kreisajā apakšējā stūrī.
"""


for row in range(8, 0, -1):
    for colon in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        print(f"{row}{colon}", end=" ")
    print()

katalogs = {"Merkurs": 0.330, "Venēra": 4.87, "Zeme": 5.97, "Marss": 0.642,
            "Jupiters": 1898, "Saturns": 568, "Urāns": 86.8, "Neptūns": 102}

for p in sorted(katalogs):
    print(p, katalogs[p])
