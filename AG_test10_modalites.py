"""


GIRONDIN AUDRIC

Test permettant de calculer le smodalités en temps linéaire 


"""
from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",10),Covid("Aude","Girondin",2000)]
lis2 = [Covid("Cyrielle", "Weiss",50), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",1999)]
lis3 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",240), Covid("Inssaf","Lakbichi",299),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",1990)]



print("La modalité de lis1 est:",calcul_modalites(lis1))
print("La modalité de lis2 est:",calcul_modalites(lis2))
print("La modalité de lis3 est:",calcul_modalites(lis3))
print("La modalité de lis4 est:",calcul_modalites(lis4))
