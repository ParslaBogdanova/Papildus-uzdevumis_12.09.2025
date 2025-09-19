import math
a = 2
print(a)
print(a * "44")
print(type(a))
# pirmais print izvada int siparu un otrs print izvada k'ada veida tips tas a mainīgais ir.


b = math.pi  # float
c = 7/2  # float
d = 7//2  # int
s = "teksts"  # string
z = 2+3j  # complex -salikts, j ir 1 = \/-1, i^2 = -1

print(type(z), type(b), type(c), type(d), type(s))
# uzdevums, samainīt mainīga vērtību vietām
x, y = 2, 3
temp = x
x = y
y = temp
print(x, y)  # izvada 3 2

n = 0b10001111  # bināra
m = 0x8f  # heksadecimāla
print(0b10001111)  # 143
print(0x8f)  # 143


# ------------------ Mainīgo tipa maiņa(TypeCasting)
s = "3.14"
print(s)
print(type(s))
print(float(s))
f = float(s)
print(int(f), type(f))

pi = 355/113
print("Pi ir " + str(pi))

print(bool(1))  # True
print(bool(0))  # False
print(bool(-3))  # True

z1 = 3+4j
r = z1.real
print(r)

s1 = 'vienkāršās pēdiņas'
s2 = "dubultās pēdiņas"
# vienalga, vai vienkāršās pēdiņas vai dubultās pēdiņas
print("vienalga, vai", s1, "vai", s2)

s3 = """Es
esmu
ļoti
garš"""
print(s3)

s = 'abcdef'
print(s)
print(s[0])  # s
print(s[1])  # b
print(s[-1])  # f
print(s[-2])  # e
print(s[1:4])  # līdz ceturtajam (neieskaitot) = bsd
# print(s[8])  # kļūda


# --------- Teksta formatēšana
a = 35500000/113
s = f"{a}"
print(s)

print(f"{a}")
print(f"{a:.2f}")
print(f"{a:.2e}")
print(f"{a:E}")

# 314159.29203539825
314159.29203539825
314159.29
3.14e+05
3.141593E+05
