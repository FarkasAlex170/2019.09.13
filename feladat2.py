#Kérjünk be két, egy napon belüli, időpontot (először az órát, aztán a percet, végül a másodpercet).
#Számítsuk ki a két időpont közti különbséget másodpercekben és írassuk ki!
hour1 = int(input ("Adja meg az első órát (0-23)"))
if hour1 < 0 or hour1 > 23:
    print("Láttál már órát?")
    exit()
minute1 =int(input ("Adja meg az első percet (0-59)"))    
if minute1 < 0 or minute1 > 59:
    print("Láttál már órát?")
    exit()
second1 = int(input ("Adja meg az első másodpercet (0-59)"))    
if second1 < 0 or second1 > 59:
    print("Láttál már órát?")
    exit()

hour2 = int(input ("Adja meg a második órát (0-23)"))
if hour2 < 0 or hour2 > 23:
    print("Láttál már órát?")
    exit()
minute2 = int(input ("Adja meg a második percet (0-59)"))
if minute2 < 0 or minute2 > 59:
    print("Láttál már órát?") 
    exit()
second2 = int(input ("Adja meg a második másodpercet (0-59)"))
if second2 < 0 or second2 > 59:
    print("Láttál már órát?")
    exit()

diffhour = (hour1-hour2) * 3600
diffmin = (minute1-minute2) * 60
diffsec = second1-second2

if diffhour < 0:
    diffhour = diffhour * -1
if diffmin < 0:
    diffmin = diffmin * -1    
if diffsec < 0:
    diffsec = diffsec * -1

print(diffhour + diffmin + diffsec , "a különbség a két megadott időpont között")           