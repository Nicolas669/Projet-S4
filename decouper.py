from couleur_pixel import*

def decouper_accept(image,boite,liste):
    '''prend en argument une image, une boite et une liste intialement vide
     et decoupe l'image en quatre boites si un obstacle est présent dans les limites
    de la boite et ainsi de suite'''
    if position_acceptable(image,boite)==True and boite.dimension() > dim_robot_max :
        liste=liste+[boite]
        return liste
    elif boite.dimension() > dim_robot_max:
        ens_boite=boite.decoupe()
        return decouper_accept(image,ens_boite[0],liste)+\
               decouper_accept(image,ens_boite[1],liste)+\
               decouper_accept(image,ens_boite[2],liste)+\
               decouper_accept(image,ens_boite[3],liste)
    return liste

#def  decouper_total(boite,liste):
#    '''prend en argument une boite et une liste intialement vide
#     et decoupe l'image en un nombre maximal de boite de taille superieure ou egale
#     aux dimensions du robot'''
#    if boite.dimension() < dim_robot_max :
#        return liste
#    if boite.dimension() > dim_robot_max :
#        liste += [boite]
#        ens_boite = boite.decoupe()
#        return decouper_total(ens_boite[0], liste) + \
#               decouper_total(ens_boite[1], liste) + \
#               decouper_total(ens_boite[2], liste) + \
#               decouper_total(ens_boite[3], liste)

#def decouper_total_petite_boite(liste):
#    """prend en entree une liste de toutes les boites possibles dans
#     mon image et renvoie seulement les boites les plus petites contenu dans la liste"""
#    taille_min = liste[0].dimension()
#    for j in range(1, len(liste)):
#        if liste[j].dimension() < taille_min:
#            taille_min = liste[j].dimension()
#    for i in liste:
#        if i.dimension()!=taille_min:
#            liste.remove(i)
#    return liste

#def decouper_acceptable_bis(listvrai,listtotal):
#    '''prend en argument deux listes de boites
#     et renvoie une liste de boites'''
#    liste=listvrai+listtotal
#    for i in liste:
#        c=0
#        for j in liste:
#            if i==j:
#                c+=1
#            if c>1:
#                liste.remove(j)
#    return liste



#listtotal=decouper_total(box,[])
#print(decouper_total_petite_boite(listtotal))
#listvrai=decouper_accept(image,box,[])
#print(decouper_acceptable_bis(listvrai,listtotal))


#    for i in listvrai:
#        for k in listtotal:
#            if not(k.getSommets()[0].getAbscisse()>=i.getSommets()[0].getAbscisse() and k.getSommets()[0].getOrdonnee()<=i.getSommets()[0].getOrdonnee() and k.getSommets()[1].getAbscisse()<=i.getSommets()[1].getAbscisse() and k.getSommets()[1].getOrdonnee()<=i.getSommets()[1].getOrdonnee() and k.getSommets()[2].getAbscisse()<=i.getSommets()[2].getAbscisse() and k.getSommets()[2].getOrdonnee()>=i.getSommets()[2].getOrdonnee() and k.getSommets()[3].getAbscisse()>=i.getSommets()[3].getAbscisse() and k.getSommets()[3].getOrdonnee()>=i.getSommets()[3].getOrdonnee()):
#                listtotal.remove(k)
#    return listtotal


#    for elt in liste:
#        c = liste.count(elt)
#        if c > 1:
#            for i in range(c - 1):
#                liste.remove(elt)
#    return liste