"""

GIRONDIN Audric

Ceci est une fichier contenant différentes fonctions, permettant :
 - d'afficher une liste
 - de lire une fichier csv
 - de faire des calculs avec des données numériques

"""


from AG_type import *
import csv 
from math import *


#Fonction d'affichage d'une liste
def affichage_liste_covid(cov):
    """
    Donnée : cov : listes de valeurs de type Covid
    Résultat : aucun
    Rôle : affiche la liste des caractéristiques contenues dans la liste cov
    """
    if (cov == []) :
        print("Retoune une Liste est vide")
    else :
         for i in range( 0, len(cov), 1):
             print(cov[i].jour, cov[i].nomReg, cov[i].incid_rea)


#Fonction Lecture d'un fichier CSV 
def lecture_fichier(nom_fichier):
    """
    Données : nom_fichier : chaîne de caractères
    Rôle : le fichier dont le nom est en paramètre
           est un fichier au format csv
           avec des ; comme séparateur.
           Chaque ligne du fichier contient une date, une région et un entier.
           La fonction lit le fichier et retourne les éléments contenues
           sous forme d'une liste Covid
    Résultat : des chaînes de caractères et des réels 
    """
#Ouverture du fichier 
    fichier = open("donnees/"+ str (nom_fichier),"r")
    lec_cov = csv.reader(fichier,delimiter=";")
    liste_covid = []
    l = lec_cov.__next__() 

#Boucle traitant chaque ligne  
    for ligne in lec_cov:
        if len(ligne)>1:
          jour = str(ligne[0])
          nomReg = str(ligne[1])
          incid_rea = int(ligne[3])
          stockage = Covid(jour, nomReg, incid_rea)
          liste_covid.append(stockage)

#Fermeture du fichier        
    fichier.close()
    return (liste_covid)

"""

Pour ces fonctions, j'ai mis en parametre "att_num" qui est une liste de type Covid
dans laquelle j'irai cherhcer mon attribut numériques "incid_rea"


"""

#Fonction pour calculer le minimum d'une liste
def minimum(att_num):
    """
    Données : att_num : liste de type Covid
    Rôle : Retourne le minimum de la liste avec les valeurs de l'attribut numérique
    Pré-conditions : liste non vide
    Résulat : un réel
    """        
    minimum = att_num[0].incid_rea
    for i in range(1,len(att_num),1):
        if minimum > att_num[i].incid_rea :
            minimum = att_num[i].incid_rea
    return minimum



#Fonction pour calculer le maximum d'une liste
def maximum(att_num):
    """
    Données : att_num : liste de type Covid
    Rôle : Retourne le maximum de la liste avec les valeurs de l'attribut numérique
    Pré-conditions : liste non vide
    Résulat : un réel 
    """
    maximum = att_num[0].incid_rea
    for i in range(1,len(att_num),1):
        if maximum < att_num[i].incid_rea :
            maximum = att_num[i].incid_rea
    return maximum



#Fonction pour calcul de moyenne
def moyenne(att_num):
    """
    Données : att_num : liste de type Covid
    Rôle : Calculer la moyenne de la liste avec la valeur de l'attribut numérique
    Pré-conditions : liste non vide
    résultat : un réel 
    """
    moyenne = 0
    moyenne_finale = 0 
    for i in range(0,len(att_num),1):
        moyenne += att_num[i].incid_rea
        moyenne_finale = moyenne/len(att_num)
    return moyenne_finale



#Fonction pour calcul de l'écart type
def ecart_type(att_num):
    """
    Données : att_num : liste de type Covid
    Rôle: Retourne l'ecart type de la liste avec la valeur de l'attribut numérique
    Résulat : un réel
    """
    m = moyenne(att_num)
    variance = 0
    ecart_type = 0
    for i in range(0,len(att_num),1):
        variance += (att_num[i].incid_rea - m)**2
    ecart_type = sqrt(variance/len(att_num))#Importation de la fonction racine carré depuis math
    return ecart_type


# Programme pour trouver le plus petit indice qui va etre reutiliser dans notre fonction de tri 
def min_indice(att_num,debut,fin):
    """
    Données : att_num : liste de type Covid
            : debut : un entier 
            : fin : un entier
    Rôle : la fonction recherche et retourne
           le plus petit indice du plus petit montant de don
           parmi les élémentsde att_num d’indices
           compris entre debut (inclus) et fin −1 (inclus)
    Résulat : un entier 
    """
    indice_mini = debut
    mini = att_num[debut].incid_rea
    for i in range(debut,fin,1):
        if att_num[i].incid_rea < mini :
           mini = att_num[i].incid_rea
           indice_mini = i
    return indice_mini
    
#Fonction de tri d'une liste par sélection du minimum 
    """
    Données : att_num : Liste de type Covide non triée
    Rôle : retourne la liste triée par sélection du minimum (ordre croisssnt)
    Résulat : Liste triée
    """

def tri_liste_par_min(att_num):
    for i in range(0,len(att_num)-1,1):
        ind_min = min_indice(att_num,i,len(att_num))
        tmp = att_num[i].incid_rea
        att_num[i].incid_rea = att_num[ind_min].incid_rea
        att_num[ind_min].incid_rea = tmp
    return att_num


#Fonction du calcul de la médiane en temps constant
def calcul_mediane(att_num):
    """
    Donnée : att_num : une liste de type Covid
    Rôle : retourne la mediane des valeurs de l'attribut numerique
    Preconditon: la liste de l'attribut numerique  doit etre triée
    Resultat : un réel
    """
    middle = len(att_num)//2
    if len(att_num) < 1:
       mediane = "Il n'y a pas de médiane"
    elif len(att_num) % 2 == 0 :
         mediane = ((att_num[middle-1].incid_rea) + (att_num[middle].incid_rea)) /2
    else:
         mediane = att_num[middle].incid_rea
    return mediane



#Fonction pour calculer les modalites d'une liste en temps linéaire
def calcul_modalites(att_num):
    """
    Donnée : att_num : une liste de type Covid
    Rôle : retourne les modalités de la liste
    Précondition: la liste doit etre triée par ordre croissant et non vide
    Résulat : un entier 
    """
    modalite = []
    modalite.append(att_num[0].incid_rea)
    i = 0
    z = 1
    while( i < len(att_num) and z < len(att_num)):
            if att_num[i].incid_rea != att_num[z].incid_rea:
                modalite.append(att_num[z].incid_rea)
                i += 1
                z += 1
            else:
                i += 1
                z += 1
    return modalite


#Fonction qui calcule le mode d'une liste 
def calcul_mode(att_num):
    """
    Donnee : att_num : une liste de type Covid 
    Rôle : retourne le mode (valeurs prises le plus de fois) dans 
    Précondition : la liste doit etre triée par ordre croissant et non vide
    Résulat : un entier 
    """
    a,b,c = 1,1,1
    for i in range(1,len(att_num),1):
        if att_num[i-1].incid_rea == att_num[i].incid_rea:
            a+=1
            if b < a:
               b = a
               c = i
        else:
            a=1
    return att_num[c].incid_rea


#Fonction d'une recherche dichotommique quelconque
def dicho_quelque (valeur_cherchee,att_num):
    """
    Donnee : att_num : une liste de type Covid
           : valeur_cherchee : valeur que l'on recherche dans la liste
    Rôle : retourne un indice quelconque dès que la valeur cherchée
           est trouvée dans la liste sinon retourne -1 si la valeur est absente 
    Précondition : la liste doit etre triée par ordre croissant et non vide
    Résulat : un entier
    """
    g = 0
    d = len(att_num)-1
    trouve = False
    while (g <= d) and not trouve :
        m = (g + d)//2
        if att_num[m].incid_rea == valeur_cherchee :
            trouve = True
        else :
            if valeur_cherchee < att_num[m].incid_rea:
                d = m -1
            else :
                g = m +1
    if trouve:
        return m
    else:
        return -1



#Fonction d'une recherche dichotommique, avec le plus petit indice
def dicho_petit (valeur_cherchee,att_num):
    """
    Donnee : att_num : une liste de type Covid
           : valeur_cherchee : valeur que l'on recherche dans la liste
    Rôle : retourne un le plus petit indice de la valeur cherchée
            dans la liste sinon retourne -1 si la valeur est absente 
    Précondition : la liste doit etre triée par ordre croissant et non vide
    Résulat : un entier
    """
    AG = 0
    g = 0
    d = len(att_num)-1
    trouve = False
    while (g <= d) and not trouve :
        m = (g + d)//2
        if att_num[m].incid_rea == valeur_cherchee :
            trouve = True
        else :
            if valeur_cherchee < att_num[m].incid_rea :
                d = m-1
            else :
                g = m+1
    if trouve : #Afin de prendre le plus petit indice de la valeur cherchee
        i = 0
        while (m-i) >= 0 and valeur_cherchee == att_num[m-i].incid_rea :
              AG = m-i
              i +=1
        return AG
    else :
        return -1

#Fonction d'une recherche dichotommique, avec le plus grand indice       
def dicho_grand(valeur_cherchee, att_num):
    """
    Donnee : att_num : une liste de type Covid
           : valeur_cherchee : valeur que l'on recherche dans la liste
    Rôle : retourne un le plus grand indice de la valeur cherchée
            dans la liste sinon retourne -1 si la valeur est absente 
    Précondition : la liste doit etre triée par ordre croissant et non vide
    Résultat : un entier
    """
    ALG = 0
    g = 0
    d = len(att_num)-1
    trouve = False
    while ( g <= d ) and not trouve :
        m = (g + d)//2
        if att_num[m].incid_rea == valeur_cherchee :
            trouve = True
        else :
            if valeur_cherchee < att_num[m].incid_rea :
                d = m-1
            else :
                g = m+1
    if trouve :#Afin de prendre le plus grand indice de la valeur cherchee
        i = 0
        while (m+i) < len(att_num)and valeur_cherchee == att_num[m+i].incid_rea :
              ALG = m+i
              i +=1
        return ALG
    else :
        return -1



#Fonction rechaerchant le nombre d'occurrences
def nb_occurrences(valeur_cherchee, att_num):
    """
    Donnee : att_num : une liste de type Covid
           : valeur_cherchee : valeur que l'on recherche dans la liste
    Rôle : retourne un le plus petit indice de la valeur cherchée
           dans la liste sinon retourne -1 si la valeur est absente 
    Précondition : la liste doit etre triée par ordre croissant et non vide
    Résultat : un entier
    """
    nombre_occurrences = 0 
    if att_num == [] or (dicho_grand (valeur_cherchee, att_num)== -1 and dicho_petit(valeur_cherchee, att_num) == -1) :
        nombre_occurrences = 0
    else :
       nombre_occurrences = dicho_grand(valeur_cherchee, att_num) - dicho_petit(valeur_cherchee, att_num)
       nombre_occurrences +=1
    return nombre_occurrences
      
