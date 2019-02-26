# Authors: Anthony Giraudo, Kari Hichma, Kilian Mac Donald, Louise Marinho
# 23 mars 2018
# main_loop_simulateur.py

"""
Simulateur du robot suiveur de ligne noir sur fond blanc

Le robot est représenté par ses 2 roues et ses 5 capteurs
Le simulateur permet de tester le comportement du robot lors :
- d'une ligne droite
- d'une ligne courbe;
- d'une intersection en croix;
- d'une impasse;
Représentés en noir sur un fond blanc

Touches du clavier pouvant etre utilisées (pour deplacer le robot vers le chemin) :
- s :
lors de l'appuie, stoppe le robot
lors du relachement, arrete de stopper le robot
- m :
lors de l'appuie, rotation du robot
lors du relachement, arret de la rotation du robot
- d :
lors de l'appuie, empeche le demi-tour du robot
lors du relachement, arret de l'empechement du demi-tour du robot
- Alt + F4 ou bouton de fermeture de fenetre : ferme la fenetre du simulateur

Le capteur du robot détecte le noir et le blanc et le robot agit en conséquence
On supposera que le terrain du simulateur est blanc avec des chemins noirs

On déterminera dans la partie parametres du robot de ce fichier,
 le choix de la direction du robot lors d'une intersection en croix

Fichiers : main_loop_simulateur.py, classes_simulateurs.py, terrain.png, champi.png, r2d2.png
"""

import pygame
from pygame.locals import *
from conversions import *
from classes_simulateur import *
import time

pygame.init()  # debut pygame

# images utilisées dans pygame pour décrire le robot
image_roue = "champi.png"
image_capteur = "r2d2.jpg"
dimensions_image_roue = (75, 75)  # en pixels
dimensions_image_capteur = (49, 49)

# parametres du robot
largeur_chemin = 40  # en pixels
l = 4 * largeur_chemin  # distance entre les deux roues en pixels
d = (12 * largeur_chemin) // 10  # distance entre les capteurs gauche droite en pixels
r = largeur_chemin  # distance entre milieu entre les roues et milieu entre les capteurs gauche droite en pixels
z = (3 * largeur_chemin) // 2  # distance entre milieu entre les deux roues et capteur central, en pixel
h = 3 * largeur_chemin // 2 + r  # distance entre milieu entre les deux roues et milieu entre les capteurs exterieur droit et exterieur gauche en pixels
i = (d * 3) // 2  # distance entre les capteurs exterieurs droits et exterieurs gauche en pixels
coeff = 100
vitesse_de_marche = pixel(0.2)
choix = "droite"  # choix de la direction lors d'une intersection en croix

# creation du robot
robot = Robot(image_roue, image_capteur, dimensions_image_roue, dimensions_image_capteur, l, d, r, z, h, i, vitesse_de_marche, coeff, largeur_chemin)

# placement initial du robot sur l'image
robot.placer(100, 500)
robot.rotation(3 * 90)

# rend transparent les contours des images correspondant aux roues et aux capteurs du robot
robot.roue_gauche.image.set_colorkey((0, 0, 0))  # image sur fond noir au depart
robot.roue_droite.image.set_colorkey((0, 0, 0))
robot.capteur_interieur_droit.image.set_colorkey((255, 255, 255))  # image sur fond blanc au depart
robot.capteur_interieur_gauche.image.set_colorkey((255, 255, 255))
robot.capteur_centre.image.set_colorkey((255, 255, 255))
robot.capteur_exterieur_droit.image.set_colorkey((255, 255, 255))
robot.capteur_exterieur_gauche.image.set_colorkey((255, 255, 255))


continuer = True  # variable de la boucle
rotation = False
stop = False
pas_demi_tour = False
t = time.clock()  # debut du temps

while continuer:  # boucle principale

    t_i = time.clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # arreter le programme en cas de fermeture de la fenetre
            continuer = False

        if event.type == pygame.KEYDOWN:  # si evement = appuie de touches de clavier
            if event.key == pygame.K_s:  # stopper le robot en cas d appui sur la touche s
                stop = True
            if event.key == K_m:  # rotation du robot en cas d appui sur la touche m
                rotation = True
            if event.key == K_d:  # empeche le demi tour en cas d appui sur la touche d
                pas_demi_tour = True

        if event.type == pygame.KEYUP:  # si evenement = relachement de touches de clavier
            if event.key == pygame.K_s:  # arreter de stopper le robot en cas de relachement de la touche s
                stop = False
            if event.key == pygame.K_m:  # arret de la rotation du robot en cas de relachement de la touche m
                rotation = False
            if event.key == pygame.K_d:  # arret de l empechement de demi tour en cas de relachement de la touche d
                pas_demi_tour = False

    if stop:  # si stop = True, stopper robot
        robot.stop()

    elif rotation:  # si rotation = True, robot fait rotation
        robot.rotation(10)

    # si virage a gauche = capteur interieur gauche detecte noir et capteur interieur droit detecte blanc
    # action du robot = tourner a gauche
    elif robot.capteur_interieur_gauche.est_dans_le_noir() and not robot.capteur_interieur_droit.est_dans_le_noir():
        robot.tourner_gauche()

    # si virage a droite = capteur interieur gauche detecte blanc et capteur interieur droit detecte noir
    # action du robot = tourner a droite
    elif robot.capteur_interieur_droit.est_dans_le_noir() and not robot.capteur_interieur_gauche.est_dans_le_noir():
        robot.tourner_droite()

    # si fin du chemin = tous les capteurs (centre, interieur, exterieur) detectent du noir
    # action du robot = arret du robot
    elif robot.capteur_interieur_gauche.est_dans_le_noir() and robot.capteur_exterieur_gauche.est_dans_le_noir() and \
            robot.capteur_interieur_droit.est_dans_le_noir() and robot.capteur_exterieur_droit.est_dans_le_noir() and \
            robot.capteur_centre.est_dans_le_noir():
        robot.stop()

    # si intersection en croix = capteurs centre et interieurs detectent noirs
    # action du robot = gerer l intersection en fonction du choix fait dans parametres du robot
    elif robot.capteur_interieur_gauche.est_dans_le_noir() and robot.capteur_interieur_droit.est_dans_le_noir() and \
            robot.capteur_centre.est_dans_le_noir():
        robot.gerer_intersection(choix)

    # si impasse = capteurs centre et interieurs detectent du blanc
    # action du robot = faire demi-tour
    elif not robot.capteur_centre.est_dans_le_noir() and not robot.capteur_interieur_droit.est_dans_le_noir() and\
            not robot.capteur_interieur_gauche.est_dans_le_noir() and not pas_demi_tour:
        pas_demi_tour = robot.demi_tour()
        t_i = time.clock()

    else:  # si ligne droite, le robot avance tout droit
        robot.tout_droit()

    # re-collage de fenetre et robot
    fenetre.blit(fond, (0, 0))
    robot.afficher()
    # rafraichissement de la fenetre
    pygame.display.flip()

    robot.mouvement(time.clock() - t_i)  # deplacement du robot

pygame.quit()  # fin pygame
