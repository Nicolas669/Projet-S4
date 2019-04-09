from parametres import*

def distance(point1,point2):
    '''prend en argument deux points et renvoi la distance entre les deux'''
    return sqrt((point1.getAbscisse()-point2.getAbscisse())**2+(point1.getOrdonnee()-point2.getOrdonnee())**2)

def appart_segment(point,droite):
    #ici une droite se reperer par une liste de deux points
    if distance(point,droite[0])+distance(point,droite[1])==distance(droite[0],droite[1]):
        return True
    else:
        return False

def adjacence(boite1,boite2):
    '''renvoie True si les deux boites en entree sont adjacentes'''
    for i in range(4):
        if appart_segment(boite1.getSommets()[i%4],[boite2.getSommets()[(i+3)%4], boite2.getSommets()[(i+2)%4]]) and appart_segment(boite1.getSommets()[(i+1)%4],[boite2.getSommets()[(i+3)%4], boite2.getSommets()[(i+2)%4]]):
            return True
        if appart_segment(boite2.getSommets()[i%4],[boite1.getSommets()[(i+3)%4], boite1.getSommets()[(i+2)%4]]) and appart_segment(boite2.getSommets()[(i+1)%4],[boite1.getSommets()[(i+3)%4], boite2.getSommets()[(i+2)%4]]):
            return True
    return False
