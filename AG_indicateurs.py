"""

GIRONDIN Audric

Ce programme affiche les differents indicateurs statistiques sous forme tabulée
pour chaque fichier CSV 

"""
from AG_listes_type import *
from AG_type import *


def tabulée(liste_covid):#création d'une fonction afin de faciliter le test 
    mini = minimum(liste_covid)
    maxi = maximum(liste_covid)
    moy = moyenne(liste_covid)
    ecart_type2 = ecart_type(liste_covid)

        
    print ("Taille du fichier:\tMinimum:\tMaximum:\tMoyenne:\tEcart_type:")
    
    print ("\t" + str(len(liste_covid))+ "\t" + "\t" + "\t" + str(mini)+"\t"
           + "\t" +  str(maxi)+"\t"+ str(moy)+ "\t" + "\t" + str(ecart_type2)
           +"\t")# j'ai effectué plusieurs retour à la ligne pour que ce ne soit pas trop longue 
    print ("\n")

def tabulée2 (liste_covid):
    mediane = calcul_mediane(liste_covid)
    mode = calcul_mode(liste_covid)

    print ("Taille du fichier:\tMediane:\tMode:")
    print ("\t" + str(len(liste_covid)) + "\t" + "\t" + "\t" + str(mediane)+ "\t"+"\t"+ str(mode))
    print ("\n")
           
#Lecture des fichiers CSV     
liste_covid1 = lecture_fichier("AG_data_5.csv")
liste_covid2 = lecture_fichier("AG_data_10.csv")
liste_covid3 = lecture_fichier("AG_data_50.csv")
liste_covid4 = lecture_fichier("AG_data_150.csv")

#Application de la fonction tableau 1
print ("\tTABLEAU DES PREMIERS INDICATEURS")
print ("\n")
tabulée(liste_covid1)
tabulée(liste_covid2)
tabulée(liste_covid3)
tabulée(liste_covid4)

print ("************************************************************************")

#Application de la fonction tableau 2
print ("\n")
print ("\tTABLEAU DES SECONDS INDICATEURS")
print ("\n")
tabulée2(liste_covid1)
tabulée2(liste_covid2)
tabulée2(liste_covid3)
tabulée2(liste_covid4)

