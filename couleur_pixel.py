from parametres import*

def position_acceptable(image,boite):
    '''prend en argument une image et une boite et renvoie False
    si un obstacle (pixel(s) noir(s)) est présent sur la partie de
    l'image delimitee par la boite et True sinon'''
    #ATTENTION un seul pixel noir constitue aussi un obstacle

    x1=boite.getSommets()[0].getAbscisse()
    x2 = boite.getSommets()[1].getAbscisse()

    y1=boite.getSommets()[0].getOrdonnee()
    y4 = boite.getSommets()[3].getOrdonnee()



    #floor sert a arrondir a l'entier inferieur

    X1=round(x1)
    X2 = round(x2)

    Y1 = round(y1)
    Y4 = round(y4)
    #le pixel a la position (i,j) est noir se traduit
    #  ici par la valeur du pixel en (i,j) est 0
    #on parcourt ici les pixels de l'image compris entre l'abscisse
    #de l'angle supérieur gauche de la boite et l'angle inférieur
    #droit de l'image
    for i in range(X1,X2):
        for j in range(Y1,Y4):
            if Image.getpixel(image, (i,j))==0:
                return False
    return True
