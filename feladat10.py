#Kérjünk be egy természetes számot ( a ), majd rajzoljunk ki a képernyőre egy háromszöget csillagokból
#( * ). A háromszög a sornyi csillagból álljon.
a = int(input("Adjon meg egy számot"))
m = a   
b = -1
for x in range(1 ,a+1):
    b = (b + 2)
    m = m - 1
    print(" " * m , b* "*" )    

