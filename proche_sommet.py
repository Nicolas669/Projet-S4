from boite_adjacence import*

def proche_sommet(liste,point):
    '''prend en entree une liste et un point et renvoi le point
    de la liste qui est le moins loins du point en entree'''
    mini=distance(liste[0],point)
    indi=0
    for j in range(len(liste)):
        if distance(liste[j],point)<mini:
            mini=distance(liste[j],point)
            indi=j
    return liste[indi]
