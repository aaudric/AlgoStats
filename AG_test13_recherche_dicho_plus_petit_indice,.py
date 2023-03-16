"""


GIRONDIN AUDRIC

Ceci est un fichier permettant de tester une recherche dichotomique,
qui trouve le plus petit indice d'une valeur présente plusieurs fois dans une liste


"""


from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",1),Covid("Aude","Girondin",10)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",50), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",4), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",9900)]


print("Test pour indice = 1")
print("La valeur recherchée de lis1 qui a le plus petit indice est :",dicho_petit(10,lis1))
print("\n")

print("Test pour valeur au début, indice = 0")
print("La valeur recherchée de lis2 qui a le plus petit indice est :",dicho_petit(50,lis2))
print("\n")

print("Test pour valeeur à la fin mais retourne le plus petit indice, indice = 2")       
print("La valeur recherchée de lis3 qui a le plus petit indice est :",dicho_petit(99,lis3))
print("\n")

print("Test pour une valeur absente, retourne -1")
print("La valeur recherchée de lis4 qui a le plus petit indice est -1"
     " car 19900 n'est pas lis4:",dicho_petit(19900,lis4))
