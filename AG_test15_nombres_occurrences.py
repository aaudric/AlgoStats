"""


GIRONDIN AUDRIC

Ceci est un fichier permettant de tester le nombre d'occurrences
d'une valeur recherchée dans une liste 


"""


from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",1),Covid("Aude","Girondin",10)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",50), Covid("Inssaf","Lakbichi",500)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",4), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",9900)]
lis5 = []

print("Test pour une occurence = 1")
print("La valeur recherchée a pour occurence dans lis1:",nb_occurrences(1,lis1))
print("\n")

print("Test pour valeur au début et au milieu, occurences = 2")
print("La valeur recherchée a pour occurence dans lis2:",nb_occurrences(50,lis2))
print("\n")

print("Test pour valeur présente plusieurs fois dont à la fin, occurences = 3")
print("La valeur recherchée a pour occurence dans lis3:",nb_occurrences(99,lis3))
print("\n")

print("Test valeur absente, aucune occurence, O ")
print("La valeur recherchée a pour occurence dans lis4: 0"
     " car elle n'est pas dans lis4:",nb_occurrences(19900,lis4))
print("\n")

print("Test pour une liste vide, aucune occurence, O ")
print("La valeur recherchée a pour occurence : 0"
     " car lis 5 est vide ",nb_occurrences(2021,lis4))


