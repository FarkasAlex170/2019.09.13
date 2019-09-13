#A program kérjen be egy számot, majd írja ki a kis szorzótáblát erre a számra (1-től 5-ig). A program a
#beolvasás után hagyjon ki egy üres sort.
numbers = [1, 2, 3, 4, 5]
valt = int(input("Adj meg egy számot!"))        
print("")
for x in numbers:
    print(" * ", x , valt , " = " , x * valt)