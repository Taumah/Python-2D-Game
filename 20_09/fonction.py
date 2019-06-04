# Créé par Thomas, le 07/09/2018 en Python 3.2

#Page des fonctions utilisées pour le jeu, sera peut etre coupées en plusieurs pages pour mieux les classer, peut etre peut etre ahah

from variables import *

import pygame
from pygame import *
from pygame import gfxdraw

import math
from math import *

import random
from random import *


def load_image(liste_nom,liste_var):
    """charge l'image demandée"""
    liste_resultats=[]                                            #generation d'une liste vide, qui va se remplir dans la boucle
    for i in range (len(liste_nom)):                              #pour chaque nom d'image dans la liste; faire:
        fichier="".join(["../Images/",liste_var[i]])              # avec "".join([variable]) on obtient tous les termes reliés en 1 seule variable. Pratique!
        liste_nom[i]=pygame.image.load(fichier).convert_alpha()   # chargement de l'image portant le nom "nomdufichier" ,avec transparence, vers la surface liste_nom[i]
        liste_resultats.append(liste_nom[i])                      #On rempli notre liste
    return liste_resultats                                        #Fin de la fonction

def texte(taille,affiche,couleur,posx,posy,fen):
    """function de texte"""
    police=pygame.font.Font(None,taille)
    text=police.render(str(affiche),1,couleur)
    position_texte=(posx,posy)
    fen.blit(text,(position_texte))

def sortir_terrain(fen,posx,posy):
    if posx>x_screen:
        posx=-5
    elif posx<0:
        posx=x_screen+5
    if posy>y_screen:
        posy=-5
    elif posy<0:
        posy=y_screen+5

    return posx,posy

def deplacer_perso_calcul(direction):        #rajouter sol: eau/sable/terre? ralentissement ? ^\__(-_-)__/^ ; #Rajouter perso, si jamais on a plusieur joueurs ou plusieurs images dispo
    """Après appui sur une flèche directionnelle la position du personnage
     est modifié"""

    hbgd=276-direction  #hbgd: hautbasgauchedroite
    decalage=deplacements[hbgd]
                                                        # Direction vaut 1,2,3 ou 4 , tout comme le nombre de tuples dans la liste deplacements
    return decalage                                     # On connait maintenant de combien on va pouvoir se déplacer


def v2_deplacer_perso(fleche):
    """fait se déplacer le perso n°2"""
    ordre=[97,100,115,119]   #valeur des touches du clavier par python
    for i in range(4):
        if fleche==ordre[i]:
            decalage=deplacements[i]
    return decalage

def deplacer_perso_nouvelle_pos(decalage,pos_x,pos_y):
    """suite de deplacer_perso_calcul"""
    pos_x+=decalage[0]
    pos_y+=decalage[1]
    return (pos_x+decalage[0],pos_y+ decalage[1])



def actualise():
    """on renome la fonction flip()"""
    display.flip()

def afficher_image(fen,nom_image,position):
    """remplace la fonction blit"""
    fen.blit(nom_image,(position[0],position[1]))


def pluie_d_etoile(fen,level):
    """afficher des objets a collecter"""

    qte_star=randint(qte_objet_lvl[level][0],qte_objet_lvl[level][1])   #nombre d'étoiles a afficher
    star_pos=[(randint(0,floor(x_screen*0.975)),randint(0,floor(y_screen*0.97))) for i in range(qte_star)]  #liste avec toutes les coordonées des etoiles sur l'écran

    return star_pos

def afficher_pluie_d_etoile(fen,objet,emplacements):
    """affichage graphique de pluie d'etoiles"""
    for i in range(len(emplacements)):
        afficher_image(fen,objet,(emplacements[i][0],emplacements[i][1]))


def score_up(fen,pos_etoile,pos_persoX,pos_persoY,score_partie):
    """ Augmente le score lorsqu'on recupere un objet """
    for position in (pos_etoile):
        if pos_persoX<=position[0]+15<=pos_persoX+30 and pos_persoY<=position[1]+15<=pos_persoY+30:  #l'image fait 30 px/30px , donc on verifie si les extrémités touchent le centre de l'objet
            score_partie+=1
            pos_etoile.remove(position)   #l'objet doit s'effacer il a été récupéré

    return score_partie,pos_etoile


def menu(fen):
    """Fonction de menu principal"""   #premiere fonction a etre appelée
    fen.fill(black)
    texte(int(0.00020*x_screen*y_screen),"Ramassez-les Tous!",orange,0.1125*x_screen,0.133*y_screen,fen)   #caler les tailles proportionellement a la taille de l'écran
    for i in range(1,4):
        gfxdraw.box(fen,(0.275*x_screen,i*0.25*y_screen+y_screen*0.033,0.5*x_screen,0.2*y_screen),orange)

        diff="Niveau  "+str(i)
        texte(int(0.00013*x_screen*y_screen),diff,black,0.4*x_screen,i*0.25*y_screen+0.1166*y_screen,fen)

    return 0

def hover_menu(fen,x_clic,y_clic):
    """Similaire a un hover en CSS, change la couleur lorsqu'on passe dessus"""


    for i in range(len(rect_menu)):
        if rect_menu[i][0]<=x_clic<=(rect_menu[i][0]+rect_menu[i][2]) and rect_menu[i][1]<=y_clic<=(rect_menu[i][1]+rect_menu[i][3]) :

            gfxdraw.box(fen,rect_menu[i],white)
            diff="Niveau  "+str(i+1)                         #  "i+1" est nécessaire car sans ca on afficherai Niveau 0 car l'indice de la premiere valeur de la liste....
            texte(int(0.00013*x_screen*y_screen),diff,black,0.4*x_screen,(i+1)*0.25*y_screen+0.1166*y_screen,fen)  #  CF ligne.116 :/
            actualise()
        else:
            gfxdraw.box(fen,rect_menu[i],orange)
            diff="Niveau  "+str(i+1)                                               #  CF ligne.116 :/
            texte(int(0.00013*x_screen*y_screen),diff,black,0.4*x_screen,(i+1)*0.25*y_screen+0.1166*y_screen,fen)  #  CF ligne.116 :/

            actualise()


def changement_page(page_origine,page_arrivee):
    return False,True


def choix_lvl(x_mouse,y_mouse):
    """Renvoie la valeur du niveau choisi"""
    lvl=-1
    for endroit in range(0,len(rect_menu)):

        if rect_menu[endroit][0]<=x_mouse<=rect_menu[endroit][0]+rect_menu[endroit][2] and rect_menu[endroit][1]<=y_mouse<=rect_menu[endroit][1]+rect_menu[endroit][3] :
            lvl=endroit
                                                                                            # lvl et i pourraient etre fusionnés mais je les garde pour plus de lisibilité
    return lvl




def animation_win(fen,liste_objets,var_jeu,score):   #des idées, des idées et encore des idées
    """animation lorsqu'on a tout récupéré"""
    if len(liste_objets)==0:    #liste vide= pas d'objets a récuperer

        fen.fill(black)
        texte(int(0.000208*x_screen*y_screen),"Gagné!",red,300,140,fen)
        texte(int(0.00017*x_screen*y_screen)," 'b' to play again ",red,350,400,fen)
        texte(int(0.00017*x_screen*y_screen)," 'l' to quit " ,red,350,500,fen)
        actualise()
        return 0,0
    else:
        return var_jeu,score


def affichage_compteur(fen,time_debut,level):
    """lance le chrono du jeu"""

    actual_time=pygame.time.get_ticks()
    time_used=actual_time-time_debut     #"temps ecoulé
    time_left=(time_left_lvl[level]-time_used)//1000   #on décompose pour mieux voir, c'est pas tres optimisé, de plus on met en secondes
    texte(40,time_left,red,720,250,fen)


def calcul_wall_pos(fen):
    """determine les posistions des murs"""    #on pourramettre +/- de murs en fonction du niveau



