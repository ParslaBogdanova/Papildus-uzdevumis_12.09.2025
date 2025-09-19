"""
1.Definēt trīs veselu skaitļu mainīgos. Veikt ar tiem 5 dažādas aritmētisku darbību kombinācijas 
pēc izvēles un izvadīt rezultātu uz ekrāna. Izvadam uz ekrāna ir pievienots arī teksts ar atšifrējumu,
piemēram, ja a=2, b=3 un c=5 uz ekrāna izvada: a+b**c = 245, kā arī (a + b)/c = 1 un vēl trīs darbības.
"""
import random
import math
a = 2
b = 3
c = 5
d = a+b**2
e = (a+b)/c
f = math.sqrt(a) + math.pi**2 - b * d
g = f // 3
h = (g + c)**3
print(d, e, f, g, h)


"""
Spiediena mērvienības.
Izveidojiet programmu, kas lietotāja ievadīto
spiedienu kPa pārveidos uz PSI, mmHg un atmosfērās.
Uz ekrāna jāizvada spiediens visās vienībās, Koeficientus 
un nepieciešamās formulas nepieciešams atrast internetā.
"""
kPa = float(input("ievadiet spiedienu kPa: "))
Pa = kPa * 10**3
atm = kPa * 0.00987
mmHg = kPa * 7.50062
PSI = kPa * 0.145038
print("kPa: " + str(kPa) + "\n"
      + "Pa: "+str(Pa) + "\n"
      + "atm: " + str(atm) + "\n"
      + "mmHg: " + str(mmHg) + "\n"
      + "PSI: " + str(PSI))


"""
Izveidot programmu, kas prasa ievadīt planētas masu un blīvumu.
Pēc šo lielumu ievades, programma uz ekrāna parāda tekstu,
kur pateikts, kāds ir planētas rādiuss.
Formula = R = \/3m/4piV
"""
m = float(input("Ievadad planētas masu: "))
b = float(input("Ievadad planētas blīvumu: "))

R1 = (3*m/(4 * math.pi * b))
R = math.pow(R1, 1/3)
# math.ceil - noapaļo skaitli/rezultātu uz tuvāko veselo.
# math.pow ir kubiska sakne
print("Planēta rādius: ", R)


"""
Skaitļu formatēšana.
Izveidot programmu, kurā ir definēts mainīgais ar skaitlisku vērtību:
daļskaitli starp 1 un 10 miljoniem (piemēram, 3412352.6234).
Programma izvada uz ekrāna šī mainīgā vērtību noformētu trīs dažādos veidos:
normālformā ar trīs zīmīgajiem cipariem un vienmēr parādītu zīmi (piemēram, +3.4e+06),
ar tūkstošiem atdalītiem ar komatu (piemēram, 3,412,352.6234) un
ar diviem cipariem aiz komata (piemēram, 3412352.62).
"""
SK = random.randint(1, 10000000)
print(f"Datora izvēlētājs: {SK}")
print(f"Normālforma: {SK:.2e}")
print(f"{SK:,}")
print(f"{SK:.2f}")
