"""

GIRONDIN Audric

Ce fichier a pour but de tester la fonction permettant de lire un fichier csv dans son ensemble

"""
from AG_type import *
from AG_listes_type import *

#TEST Fonction lecture_fichier CSV
def test_lecture(liste_covid):
    print("Ce programme teste la lecture d'un fichier CSV contenant",len(liste_covid)," lignes de données")
    if len(liste_covid)<= 20 :
        print("\n")
        affichage_liste_covid(liste_covid)
        print("\n")
       
    else :
       print("Ce fichier est trop grand, il contient", len(liste_covid) ,"lignes de données")
       print("\n")

#Test pour fichier avec 5 lignes de données
liste_covid = lecture_fichier("AG_data_5.csv")
test_lecture(liste_covid)

#Test pour ficher contenant 10 lignes de données 
liste_covid2 =  lecture_fichier("AG_data_10.csv")
test_lecture(liste_covid2)

#Test pour fihier contenant 50 lignes de données
liste_covid3 =  lecture_fichier("AG_data_50.csv")
test_lecture(liste_covid3)

#Test pour fichier contenant 150 lignes de données
liste_covid4 =  lecture_fichier("AG_data_150.csv")
test_lecture(liste_covid4)

#Test pour un fichier vide
liste_covid5 =  lecture_fichier("AG_data_0.csv")
test_lecture(liste_covid5)
