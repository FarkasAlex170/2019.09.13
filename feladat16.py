#Készítsünk programot, amely bekér egy mondatot, majd kiírja ugyanezt a mondatot úgy, hogy mindegyik
#betű (karakter) után kirak egy szóközt.
sentence = (str(input("Irjon be egy mondatot!")))
for x in range(len(sentence)):
    print(sentence[x], end = " ")
print()    
