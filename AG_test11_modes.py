"""

GIRONDIN AUDRIC


Ce test permet de définir le mode de chaque liste

"""
from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",10),Covid("Aude","Girondin",10)]
lis2 = [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99)]
lis3= [Covid("Cyrielle", "Weiss",24), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]



print("Le mode de lis1 est:",calcul_mode(lis1))
print("La mode de lis2 est:",calcul_mode(lis2))
print("La mode de lis3 est:",calcul_mode(lis3))
