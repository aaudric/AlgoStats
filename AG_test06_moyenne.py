"""

GIRONDIN Audric

Grace à ce test, on peut s'assurer que la fonction moyenne fonctionne correctement,
Celle-ci calcule la moyenne des éléments d'une liste

"""


from AG_listes_type import *

#Utilisation de différents listes, pour avoir difféérents cas de test

lis1 = [Covid("Girondin", "Audric",109),Covid("Aude","Girondin",1)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",5000), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",990),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",400), Covid("Edlyne", "Lolia",246), Covid("Inssaf","Lakbichi",999),Covid("Girondin", "Audric",9900),Covid("Aude","Girondin",99)]

print("Test pour la moyenne de lis1, moyenne attendue = 55")
print("Le moyenne de lis 1 est :",moyenne(lis1))
print("\n")

print("Test pour le moyenne de lis2, moyenne attendue = 1850")
print("Le moyenne de lis 2 est :",moyenne(lis2))
print("\n")

print("Test pour le moyenne de lis3, moyenne attendue = 290.4")
print("Le moyenne de lis 3 est :",moyenne(lis3))
print("\n")

print("Test pour la moyenne de lis4, moyenne attendue = 2328.8")
print("Le moyenne de lis 4 est :", moyenne(lis4))

