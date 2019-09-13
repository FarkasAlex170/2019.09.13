#Készítsünk programot, amely kiszámolja az első 100 db természetes szám összegét, majd kiírja az
#eredményt. (Az összeg kiszámolásához vezessünk be egy változót, amelyet a program elején kinullázunk,
#a ciklusmagban pedig mindig hozzáadjuk a ciklusváltozó értékét, tehát sorban az 1, 2, 3, 4, ..., 100
#számokat.)
i = int(0)
for x in range(1, 101):
    i = x + i
print(i)    

