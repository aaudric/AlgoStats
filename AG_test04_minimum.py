"""

GIRONDIN Audric

Ce fichier permet de tester si la fonction minimum est correcte,
IL affiche le plus petit élément de la liste 

"""


from AG_listes_type import *

#Utilisation de différents listes, pour avoir difféérents cas de test 

lis1 = [Covid("Girondin", "Audric",109),Covid("Aude","Girondin",1)]
lis2 = [Covid("Cyrielle", "Weiss",5000), Covid("Edlyne", "Lolia",50), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",990),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",400), Covid("Edlyne", "Lolia",246), Covid("Inssaf","Lakbichi",999),Covid("Girondin", "Audric",9900),Covid("Aude","Girondin",99)]

print("Test pour le minimum à la fin, minimum = 1")
print("Le minimum de lis 1 est :",minimum(lis1))
print("\n")

print("Test pour le minimum au milieu, minimum = 50")
print("Le minimum de lis 2 est :",minimum(lis2))
print("\n")

print("Test pour le minimum au début, minimum = 24")
print("Le minimum de lis 3 est :",minimum(lis3))
print("\n")

print("Test pour le minimum à la fin, minimum = 99")
print("Le minimum de lis 4 est :", minimum(lis4))
