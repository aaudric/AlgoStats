"""

GIRONDIN AUDRIC

Ce fichier permet de tester la fonction d'une recherche dichotommique quelconque,
Elle retourne l'indice qu'elle trouve en premier 

"""


from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",10),Covid("Aude","Girondin",2000)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",50), Covid("Inssaf","Lakbichi",1999)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",4), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",9900)]


print("Test pour valeur au début, indice = 0")
print("La valeur recherchée de lis1 est d'indice :",dicho_quelque(10,lis1))
print("\n")

print("Test pour valeur présente au début et au milieu, retourne un indice quelconque, indice = 1")
print("La valeur recherchée de lis2 est d'indice :",dicho_quelque(50,lis2))
print("\n")

print("Test pour valeur présente plusieurs fois dont une a la fin, indice quelconque = 2")
print("La valeur recherchée de lis3 est d'indice :",dicho_quelque(99,lis3))
print("\n")

print("Test pour valeur absente, retourne -1")
print("La valeur recherchée de lis4 est d'indice :",dicho_quelque(19900,lis4))

 
