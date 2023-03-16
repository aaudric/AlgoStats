"""

GIRONDIN Audric

Ce fichier permet de tester une fonction qui a pour but d'afficher une liste 

"""


from AG_type import *
from AG_listes_type import *

#Liste est là pour tester l'affichage d'une liste à plusieurs éléments 
liste = [Covid("Girondin", "Audric",10), Covid("Cyrielle", "Weiss",00), Covid("Edlyne", "Lolia",24)]
print("TEST pour une liste à plusieurs éléments:")
affichage_liste_covid(liste)
print("\n")

#Liste2, afin de tester l'affichage d'une liste à un élément
liste2 = [Covid("Girondin", "Audric",10)]
print("TEST pour une liste à 1 élément:")
affichage_liste_covid(liste2)
print("\n")

#LIste3, afin de tester une liste vide 
liste3 = []
affichage_liste_covid(liste3)
