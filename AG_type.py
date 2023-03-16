"""
GIRONDIN Audric

Ce fichier comporte une déclaration de nouveau type (Covid)
et une fonction permettant d'afficher une instance du type 
"""
class Covid(object):
    def __init__(self, valeur_jour, valeur_nomReg, valeur_incid_rea):
        self.jour = valeur_jour
        self.nomReg = valeur_nomReg
        self.incid_rea = valeur_incid_rea



def affichage_covid(covid19):
    """
    Données : covid19 : liste de type Covid
    Rôles : Permet d'afficher les caractéristiques de Covid
           : jour : attribut non numérique
           : NomReg : attribut numérique
           : incid_rea : attribut numérique
    Résultat : une instance 
    """
    print(covid19.jour, covid19.nomReg, covid19.incid_rea)

