"""


GIRONDIN AUDRIC

Ceci est un fichier permettant de tester une recherche dichotomique,
qui trouve le plus grand indice d'une valeur présente plusieurs fois dans une liste 


"""


from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",1),Covid("Aude","Girondin",1)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",50), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",4), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",9900)]


print("Test pour valeur au début et a la fin, indice = 1")
print("La valeur recherchée de lis1 qui a le plus grand indice est :",dicho_grand(1,lis1))
print("\n")

print("Test pour valeur au début et au milieu, indice = 1")
print("La valeur recherchée de lis2 qui a le plus grand indice est :",dicho_grand(50,lis2))
print("\n")

print("Test pour valeur à la fin, indice = 4")
print("La valeur recherchée de lis3 qui a le plus grand indice est :",dicho_grand(99,lis3))
print("\n")

print("Test valeur absente, retourne -1")
print("La valeur recherchée de lis4 qui a le plus grand indice est -1"
     " car 19900 n'est pas lis4:",dicho_grand(19900,lis4))
