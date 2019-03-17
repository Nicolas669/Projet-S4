
from class_point import *
from class_graph import*


# fonction qui recherche le sommet le plus proche du départ parmi ceux non marqués
# L_dis est la liste des distances au point de départ
def recherche_plus_proche(L_marques ,L_dis):
    dmin = inf
    plus_proche = -1
    for i, d in enumerate(L_dis):
        if L_marques[i] == False and d < dmin:
            plus_proche = i
            dmin = d
    return plus_proche


# sélectionne le sommet le plus proche du point de départ (indpp) et met à jour les distances de ses voisins non marqués, puis marque indpp.
# si indpp est le sommet d'arrivée, met fin à la boucle de la fonction algo.
def actualisation(G, L_sommets, L_marques, L_dis, chem, arrive):
    n = len(L_sommets)
    indpp = recherche_plus_proche(L_marques, L_dis)

    if indpp != -1 and indpp != arrive:
        dis_som_origine = L_dis[indpp]
        for a in G[indpp]:
            sp, dis_sommet_sp = a
            idsp = L_sommets.index(sp)
            if L_marques[idsp] == False:
                if L_dis[idsp] > dis_sommet_sp + dis_som_origine:
                    L_dis[idsp] = dis_sommet_sp + dis_som_origine
                    chem[idsp] = indpp
        L_marques[indpp] = True
        return (True)
    else:
        return (False)


# Détermine la distance de chaque sommet du graphe par rapport au sommet de départ, jusqu'à ce que le sommet d'arrivée soit sélectionné.
# Pour faire référence à un sommet, on utilisera son indice dans la liste L_sommets.
def algo(Graphe, dep, arr):
    L_sommets = Graphe.getVertices()
    if dep not in L_sommets or arr not in L_sommets:
        return "point de départ ou arrivée hors du graphe"
    G = Graphe.successeurs()
    n = len(G)
    inddep = L_sommets.index(dep)
    indarr = L_sommets.index(arr)
    L_MARQUE = [False] * n
    L_DIS = [inf] * inddep + [0] + [inf] * (n - inddep - 1)
    CHEM = [-3] * inddep + [- 1] + [-3] * (n - inddep - 1)
    cont = True
    while cont:
        cont = actualisation(G, L_sommets, L_MARQUE, L_DIS, CHEM, indarr)

    # retrouve le chemin le plus court en partant du sommet d'arrivée et en allant jusqu'au sommet de départ (CHEM donne l'indice du sommet précédent de chaque sommet dans le chemin)
    res = [arr]
    k = indarr
    while k != inddep:
        res = [L_sommets[CHEM[k]]] + res
        k = CHEM[k]
    return res


# inf est valeur représentant la distance infinie

inf = 1000
p0 = Point(0, 0)
p1 = Point(0, 1)
p2 = Point(2, 0)
p3 = Point(0, 4)

h = Graph([p0, p1, p2, p3], [(p0, p1, 5.0), (p0, p2, 1.0), (p1, p2, 3.0), (p1, p3, 1.0), (p2, p3, 1.0), (p0, p3, 3.0)])
print(algo(h, p0, p1))
