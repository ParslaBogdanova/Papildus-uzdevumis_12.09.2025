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
