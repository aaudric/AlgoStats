"""

GIRONDIN Audric

On cherche à voir si la fonction maximum s'éxécute convenablement ,
Elle doit afficher l'élément le plus grand de la liste

"""

from AG_listes_type import *

#Utilisation de différents listes, pour avoir difféérents cas de test

lis1 = [Covid("Girondin", "Audric",109),Covid("Aude","Girondin",1)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",5000), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",990),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",400), Covid("Edlyne", "Lolia",246), Covid("Inssaf","Lakbichi",999),Covid("Girondin", "Audric",9900),Covid("Aude","Girondin",99)]

print("Test pour le maximum au début, maximum = 109")
print("Le maximum de lis 1 est :",maximum(lis1))
print("\n")

print("Test pour le maximum au milieu, maximum = 5000")
print("Le maximum de lis 2 est :",maximum(lis2))
print("\n")

print("Test pour le maximum au ilieu entre plusieurs valeurs, maximum = 990")
print("Le minimum de lis 3 est :",maximum(lis3))
print("\n")

print("Test pour le maximum placé au hasard, maximum = 9900")
print("Le maximum de lis 4 est :", maximum(lis4))

