from decouper import*
from proche_sommet import*

def cree_map(image,box,name,point_depart,point_arrivee):

    pygame.init()

    resVrai=decouper_accept(image,box,[]) #on recupere la liste de toutes
    # les boites une fois l'image decoupee
    resMil=[]
    #Ouverture de la fenêtre Pygame
    fenetre= pygame.display.set_mode(taille)
    #Chargement et collage du fond
    fond=  pygame.image.load(name)
    fenetre.blit(fond, (0,0))

    #Rafraîchissement de l'écran
    pygame.display.flip()

    for i in range (len(resVrai)):
        pygame.draw.rect(fenetre,(50,250,50), [resVrai[i].getSommets()[0].getAbscisse(),
                                             resVrai[i].getSommets()[0].getOrdonnee(),
                                             resVrai[i].dimension()[0],
                                             resVrai[i].dimension()[1]], 4)
        #on a affiche les rectangle, maintenant on affiche le graphe:
        resMil+=[resVrai[i].getSommets()[0].milieu(resVrai[i].getSommets()[2])]
        pygame.draw.circle(fenetre,(255, 127, 0),[round(resMil[i].getAbscisse()),round(resMil[i].getOrdonnee())],8)

    point_de_contact_dep=proche_sommet(resMil,point_depart)
    pygame.draw.line(fenetre, (255, 127, 0), [round(point_de_contact_dep.getAbscisse()), round(point_de_contact_dep.getOrdonnee())],
                     [round(point_depart.getAbscisse()), round(point_depart.getOrdonnee())], 5)
    point_de_contact_arr = proche_sommet(resMil, point_arrivee)
    pygame.draw.line(fenetre, (255, 127, 0),
                     [round(point_de_contact_arr.getAbscisse()), round(point_de_contact_arr.getOrdonnee())],
                     [round(point_arrivee.getAbscisse()), round(point_arrivee.getOrdonnee())], 5)
    pygame.draw.circle(fenetre, (0, 0, 255), [point_depart.getAbscisse(), point_depart.getOrdonnee()], 8)
    pygame.draw.circle(fenetre, (0, 0, 255), [point_arrivee.getAbscisse(), point_arrivee.getOrdonnee()], 8)
    aretes=[]
    for j in range(len(resVrai)):
        for k in range(len(resVrai)):
            if adjacence(resVrai[j], resVrai[k]):
                pygame.draw.line(fenetre, (255, 127, 0), [round(resMil[j].getAbscisse()),round(resMil[j].getOrdonnee())], [round(resMil[k].getAbscisse()),round(resMil[k].getOrdonnee())],5)
                if (resMil[j],resMil[k],distance(resMil[j],resMil[k])) and (resMil[k],resMil[j],distance(resMil[j],resMil[k])) not in aretes:
                    aretes+=(resMil[j],resMil[k],distance(resMil[j],resMil[k])),
    graphe=Graph(resMil,aretes)
    graphe.add_edge(point_depart,point_de_contact_dep,distance(point_de_contact_dep,point_depart))
    graphe.add_edge(point_arrivee, point_de_contact_arr, distance(point_de_contact_arr, point_arrivee))
    # Rafraichissement
    pygame.display.flip()
    pygame.image.save(fenetre,nom_map)
    return graphe

