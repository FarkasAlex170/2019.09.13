#Készítsünk programot, amely kiszámolja az első 100 db páratlan szám összegét. (A ciklust vegyük egytől
#százig, majd a ciklusmagban vegyük a ciklusváltozó kétszeresét eggyel csökkentve - így megkapjuk a
#páratlan számokat. Ezeket hasonlóan adjuk össze, mint az első feladatban).
i = 0
g = 0
for x in range(1 ,101):
    i = x * 2 -1
    g = i + x
print(g)    
