from class_point import *
from math import sqrt

class Boite:
    """ On ne considere ici que des boites rectangulaires ABCD, A étant le point en haut à gauche """
    def __init__(self, liste_sommets):
        self.sommets = liste_sommets

    def getSommets(self):
        return self.sommets

    def setSommets(self, values):
        assert isinstance(values, list)
        for i in values:
            assert isinstance(i, Point)
        self.sommets = values

    def __eq__(self, other):
        assert isinstance(other, Boite)
        return self.sommets == other.sommets

    def decoupe(self):
        """ None --> Liste de 4 boites
         Découpe une boite rectangulaire ABCD, de centre 0 en 4 boites """
        pointA = self.getSommets()[0]
        pointB = self.getSommets()[1]
        pointC = self.getSommets()[2]
        pointD = self.getSommets()[3]
        pointO = pointA.milieu(pointC)
        pointAB = pointA.milieu(pointB)
        pointBC = pointB.milieu(pointC)
        pointCD = pointC.milieu(pointD)
        pointDA = pointD.milieu(pointA)
        boiteA = Boite([pointA, pointAB, pointO, pointDA])
        boiteB = Boite([pointAB, pointB, pointBC, pointO])
        boiteC = Boite([pointO, pointBC, pointC, pointCD])
        boiteD = Boite([pointDA, pointO, pointCD, pointD])
        return [boiteA, boiteB, boiteC, boiteD]

    def dimension(self):
        """ None --> liste (longueur AB, largeur BC) """
        pointA = self.getSommets()[0]
        pointB = self.getSommets()[1]
        pointC = self.getSommets()[2]
        longueur = sqrt((pointB.getAbscisse() - pointA.getAbscisse())**2 + (pointB.getOrdonnee() - pointA.getOrdonnee())**2)
        largeur = sqrt((pointB.getAbscisse() - pointC.getAbscisse())**2 + (pointB.getOrdonnee() - pointC.getOrdonnee())**2)
        return [longueur, largeur]
