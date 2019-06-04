# Créé par Thomas, le 07/09/2018 en Python 3.2

#Contient le texte principal du jeu ;) , il récupère (à sens unique) les informations des fichiers.py fonctions et variables

import pygame
from pygame import *
from pygame.locals import *
from fonction import *
from variables import *
import random
from random import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((x_screen,y_screen))

fenetre.fill(white)   # ^Fenetre blanche
actualise()

orientation_perso=load_image(dk_names,images_names)  #chargement de la liste des images
objets_utiles=load_image(checkpoint_names,checkpoint_fichier)
back_and_wall=load_image(back_names,back_fichier)   #liste: fond, mur_vertical,mur horizontal



pygame.key.set_repeat(200,200)

menu(fenetre)
actualise()
continuer = 1
while continuer:

    if var_menu==True and actualise_once_menu==True:
        menu(fenetre)
        actualise()
        actualise_once_menu=False      # pour s'assurer qu'on n'actualise qu'une fois et eviter de créer des clignotants

    if var_jeu==True :
        fenetre.fill(white)

        afficher_image(fenetre,back_and_wall[0],(0,0))   #fond
        afficher_image(fenetre,orientation_perso[1],(position_dk_X,position_dk_Y)) #le parametre n°2 est l'image a afficher
        afficher_image(fenetre,orientation_perso[4],(position_dk_X_2,position_dk_Y_2))
        afficher_pluie_d_etoile(fenetre,objets_utiles[0],placement_etoiles)     #pour effacer les objets au premier contact, il faut reordonner les fonctions :*

        txt_score="Score :"+"   "+str(score_dk)+"  "+"/"+str(len(placement_etoiles)+score_dk)  # quand on prend 1point on retire une valeur de la liste placement etoile, la somme des deux est donc constante
        texte(30,txt_score,black,x_screen*0.8,y_screen*0.93,fenetre)
        txt_lvl="Niveau  "+ str(level+1)
        texte(30,txt_lvl,black,x_screen*0.8,y_screen*0.07,fenetre)
        if chrono_demarre==1:
            affichage_compteur(fenetre,time_debut,level)

        actualise()

    for event in pygame.event.get():	#Attente des événements

        if event.type==MOUSEMOTION and var_menu==True :
            x_mouse,y_mouse=pygame.mouse.get_pos()
            hover_menu(fenetre,x_mouse,y_mouse)

        if event.type==MOUSEBUTTONDOWN and event.button==1 and var_menu==True :
            x_mouse,y_mouse=pygame.mouse.get_pos()
            level=choix_lvl(x_mouse,y_mouse)
            print("level: ",level)
            if level==0 or level==1 or level==2:
                var_menu,var_jeu=changement_page(var_menu,var_jeu)    #l'un passe a false et l'autre a true, on economise des lignes

                placement_etoiles=pluie_d_etoile(fenetre,level)            #preparation de la liste de objets à récupérer



        if event.type== KEYDOWN and (event.key==K_UP or event.key==K_DOWN or event.key==K_RIGHT or event.key==K_LEFT) and var_jeu==True:   #HAUT BAS DROITE HAUCHE 273 274 275 276 ordre!
            direction=event.key

            if chrono_demarre==0:
                time_debut=pygame.time.get_ticks()
                chrono_demarre=1


            bouger_perso=deplacer_perso_calcul(direction)  #tuple comportant les déplacement en X et Y
            position_dk_X,position_dk_Y=deplacer_perso_nouvelle_pos(bouger_perso,position_dk_X,position_dk_Y)  #la fonction sort un tuple, décomposé en 2variables séparées
            position_dk_X,position_dk_Y=sortir_terrain(fenetre,position_dk_X,position_dk_Y)

            score_dk,placement_etoiles=score_up(fenetre,placement_etoiles,position_dk_X,position_dk_Y,score_dk)

            actualise()
            var_jeu,score_dk=animation_win(fenetre,placement_etoiles,var_jeu,score_dk)       # tant qu'on ne gagne pas, on affecte aux variables les valeurs de celles ci avant d'entrer dans la fonction

        elif event.type==KEYDOWN and event.key==K_r and var_jeu==True:
            score_dk=0                             #nouvelle partie, remise a 0 du score
            fenetre.fill(white)
            placement_etoiles=pluie_d_etoile(fenetre,level)   #On change la liste des positions

            afficher_image(fenetre,orientation_perso[1],(position_dk_X,position_dk_Y)) #le parametre n°2 est l'image a afficher
            afficher_pluie_d_etoile(fenetre,objets_utiles[0],placement_etoiles)     #le parametre n°2 est l'image a afficher

            txt_score="Score :"+"   "+str(score_dk)+"  "+"/"+str(len(placement_etoiles))
            texte(30,txt_score,black,x_screen*0.8,y_screen*0.93,fenetre)
            txt_lvl="Niveau  "+ str(level+1)
            texte(30,txt_lvl,black,x_screen*0.8,y_screen*0.07,fenetre)


            score_dk,placement_etoiles=score_up(fenetre,placement_etoiles,position_dk_X,position_dk_Y,score_dk)
            actualise()

        elif event.type== KEYDOWN and (event.key==K_w or event.key==K_a or event.key==K_s or event.key==K_d) and var_jeu==True:
            direction=event.key
            if chrono_demarre==0:
                time_debut=pygame.time.get_ticks()
                chrono_demarre=1


            bouger_perso=v2_deplacer_perso(direction)  #tuple comportant les déplacement en X et Y
            position_dk_X_2,position_dk_Y_2=deplacer_perso_nouvelle_pos(bouger_perso,position_dk_X_2,position_dk_Y_2)  #la fonction sort un tuple, décomposé en 2variables séparées
            position_dk_X_2,position_dk_Y_2=sortir_terrain(fenetre,position_dk_X_2,position_dk_Y_2)

            score_dk,placement_etoiles=score_up(fenetre,placement_etoiles,position_dk_X_2,position_dk_Y_2,score_dk)

            actualise()
            var_jeu,score_dk=animation_win(fenetre,placement_etoiles,var_jeu,score_dk)       # tant qu'on ne gagne pas, on affecte aux variables les valeurs de celles ci avant d'entrer dans la fonction



        if (event.type==KEYDOWN and event.key==K_b) and var_menu!=True :

            var_menu=True
            var_jeu=False
            actualise_once_menu=True     #On réinitialise tout, TOUT, TOUUUUUUT !!
            score_dk=0                    #surtout le score
            chrono_demarre=0
            position_dk_X=400
            position_dk_Y=300

        if (event.type == QUIT or (event.type==KEYDOWN and event.key==K_l)) :
            continuer = 0
            pygame.quit()


