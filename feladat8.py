#Készítsünk programot, amely kiszámolja az első 100 db páros szám összegét. (A ciklust vegyük egytől
#százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét - így megkapjuk a páros számokat.
#Ezeket hasonlóan adjuk össze, mint az első feladatban.)
i = 0
g = 0
for x in range(1, 101):
    i = x * 2
    g = i + g
print(g)
