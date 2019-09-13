#Kérjünk be egy keresztnevet, majd írassuk ki ezt a nevet betűnként függőlegesen lefelé a képernyőre.
#Például ha megadjuk névnek a "Peti"-t, a program írja ki ezt
last_name = str(input("Add last name: "))
for x in range(len(last_name)):
    print(last_name[x])
