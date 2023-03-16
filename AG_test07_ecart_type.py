"""

GIRONDIN Audric

Permet de vérifier que la fonction écart type calcule bien cette derniere

"""


from AG_listes_type import *

#Utilisation de différents listes, pour avoir difféérents cas de test

lis1 = [Covid("Girondin", "Audric",109),Covid("Aude","Girondin",1)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",5000), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",990),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",400), Covid("Edlyne", "Lolia",246), Covid("Inssaf","Lakbichi",999),Covid("Girondin", "Audric",9900),Covid("Aude","Girondin",99)]

print("Test pour l'écart type  de lis1, écart type attendue = 54")
print("L'écart type de lis 1 est :",ecart_type(lis1))
print("\n")

print("Test pour l'écart type de lis2, écart type attendue = 2234.949")
print("L'écart type de lis 2 est :",ecart_type(lis2))
print("\n")

print("Test pour l'écart type de lis3, écart type attendue = 356.711")
print("L'écart type de lis 3 est :",ecart_type(lis3))
print("\n")

print("Test pour l'écart type de lis4, écart type attendue = 3797.940")
print("L'écart type de lis 4 est :", ecart_type(lis4))

