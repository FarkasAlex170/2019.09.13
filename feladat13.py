#Állítsuk elő és írassuk ki az első N darab Fibonacci-számot. Ennek a sorozatnak az a jellemzője, hogy
#bármelyik eleme egyenlő az előző kettő összegével. A sorozat néhány eleme: 1, 1, 2, 3, 5, 8, 13,

numof = int(input("hany elemig irja ki a fibonacci számokat?:" ))
a = 0
b = 1
c = a+b

for x in range(numof):
    a = b
    b = c
    c = b+c
    d = c+b
print(d)      