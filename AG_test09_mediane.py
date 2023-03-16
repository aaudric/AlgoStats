"""

GIRONDIN AUDRIC


Ce test a pour but de calculer la médiane d'une liste supposéee triéefrom AG_listes_type import *
"""

from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",10),Covid("Aude","Girondin",20),Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",190)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",190)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = []

print("La médiane de lis1 est:",calcul_mediane(lis1))
print("\n")

print("La médiane de lis2 est:",calcul_mediane(lis2))
print("\n")

print("La médiane de lis3 est:",calcul_mediane(lis3))
print("\n")

print("La médiane de lis4 est:",calcul_mediane(lis4))



