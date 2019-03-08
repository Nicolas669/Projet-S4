
#transforme un pavage en graphe
def correspondance(centres,adjacences,départ,arrivée):
    pass



#fonction qui recherche le sommet le plus proche du départ parmi ceux non marqués
#L_dis est la liste des distances aux points de départ
def recherche_plus_proche(L_marques,L_dis):
    dmin=inf
    plus_proche=-1
    for i,d in enumerate(L_dis):
        if L_marques[i]==False and d<dmin:
            plus_proche=i
            dmin=d
    return plus_proche

#sélectionne le sommet le plus proche du point de départ et met à jour les distances au départ de ses voisins non marqués, puis le marque
def actualisation(G,L_marques,L_dis,chem):
    # G = graphe.successeurs()
    n=len(G)
    sommet=recherche_plus_proche(L_marques,L_dis)

    if sommet!=-1 and sommet!=n-1:
        dis_som_origine=L_dis[sommet]
        for a in G[sommet]:
            sp,dis_sommet_sp=a
            if L_marques[sp]==False:
                if L_dis[sp]>dis_sommet_sp+dis_som_origine:
                    L_dis[sp]=dis_sommet_sp+dis_som_origine
                    chem[sp]=sommet
        L_marques[sommet]=True

        return(True)
    else:
        return(False)

#détermine les distances au départ des sommets du graphe jusqu'à ce que le sommet d'arrivée soit sélectionné
def algo(G):
    n=len(G)
    L_MARQUE=[False]*n
    L_DIS=[0]+[inf]*(n-1)
    CHEM=[-1]+[-3]*(n-1)
    cont=True
    while cont:
        cont=actualisation(G,L_MARQUE,L_DIS,CHEM)

    #retrouve le chemin le plus court en partant du sommet d'arrivée (n-1) et en allant jusqu'au sommet de départ (0)
    res=[n-1]
    k=n-1
    while k!=0:
        res=[CHEM[k]]+res
        k=CHEM[k]
    return res


#inf est valeur représentant la distance infinie
inf=1000
EX=[[(1,1),(2,4)],[(0,1),(3,2),(5,1)],[(0,4),(3,2),(4,1)],[(1,2),(2,2),(4,1)],[(2,1),(3,1),(5,3)],[(1,1),(4,3),(6,2)],[(5,2)]]
EX2=[[(1,8),(3,21),(4,17)],[(0,8),(2,8)],[(1,8),(6,25)],[(0,21),(5,20),(8,10)],[(0,17),(7,50)],[(3,20)],[(2,25),(7,8)],[(6,8),(8,16),(4,50)],[(3,10),(7,16),(9,9)],[(8,9)]]
print(algo(EX2))
