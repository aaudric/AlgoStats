"""

GIRONDIN AUDRIC

Test qui trie une liste quelconque par ordre croissant 

"""


from AG_listes_type import *

lis1 = [Covid("Girondin", "Audric",20),Covid("Aude","Girondin",10)]
lis2 = [Covid("Cyrielle", "Weiss",214), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99)]
lis3= [Covid("Cyrielle", "Weiss",240), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",990),Covid("Girondin", "Audric",99),Covid("Aude","Girondin",99)]
lis4 = [Covid("Cyrielle", "Weiss",4), Covid("Edlyne", "Lolia",24), Covid("Inssaf","Lakbichi",99),Covid("Girondin", "Audric",998),Covid("Aude","Girondin",9900)]


print("Lis1 triée devient, malgré la plus grande valeur est au début dans  liste initiale :\n")
affichage_liste_covid(tri_liste_par_min(lis1))
print("\n")

print("Lis2 triée est devient, malgré la plus grande valeur est au milieu dans  liste initiale :\n")
affichage_liste_covid(tri_liste_par_min(lis2))
print("\n")

print("Lis3 triée devient  malgré la plus grande valeur est entre plusieurs dans  liste initiale :\n") 
affichage_liste_covid(tri_liste_par_min(lis3))
print("\n")

print("Lis3 triée devient  malgré la plus grande valeur est à la fin dans  liste initiale :\n") 
affichage_liste_covid(tri_liste_par_min(lis4))
