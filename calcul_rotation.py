_author_ = "Nicolas Coruzzi"
_filename_ = "calcul_rotation"
_creationdate_ = "25/03/19"

import numpy as np
from boite_adjacence import distance
import math
from class_point import*

def angle(centre,p2,p3):
    '''Prend en entrée trois points réprésentant deux vecteurs partageant
     un même point et retourne la valeur en degré de l'angle entre les deux'''

    x1=centre.getAbscisse()
    y1=centre.getOrdonnee()

    x2=p2.getAbscisse()
    y2=p2.getOrdonnee()

    u= np.array([x2-x1,y2-y1])

    x3=p3.getAbscisse()
    y3=p3.getOrdonnee()


    v=np.array([x3-x1,y3-y1])

    prod_scal=np.dot(u,v)
    norme1=distance(centre,p2)
    norme2=distance(centre,p3)
    return math.degrees(math.acos(prod_scal/(norme1*norme2)))

print(angle(Point(0,0),Point(1,0),Point(0,1)))