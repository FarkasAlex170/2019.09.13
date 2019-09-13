#Kérjünk be két természetes számot ( M , N ), majd rajzoljunk ki a képernyőre egy M x N méretű
#téglalapot csillag ( * ) jelekből úgy, hogy a téglalap belseje üres legyen. (Aka.: disznó ól csillagból
#feladat.)
M = int(input("Adjon meg egy számot!"))
N = int(input("Adjon meg még egy számot!"))
for i in range(1, n+1): 
    for j in range(1, m+1) : 
        if (i == 1 or i == n or
            j == 1 or j == m) : 
            print("*", end="")             
        else : 
            print(" ", end="")             
      
    print() 