# Créé par Thomas, le 07/09/2018 en Python 3.2

#pages des variables, qui sera méliorée au cours du jeu et mieux organisée

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~COULEURS~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
orange=(255,130,0)
purple=(160,0,255)
yellow=(255,255,0)

#------------------------------------------------#

score_dk=0   # score initial

images_names=["dk_gauche.png","dk_bas.png","dk_droite.png","dk_haut.png","dk_droite_duo.png"]   #nom des fichier .jpeg/.PNG ... images
dk_names=["perso_gauche","perso_bas","perso_droite","perso_haut","perso2_droite"]           #Variables qui comportent les différentes positions de dk

checkpoint_fichier=["arrivee.png","depart.png","mur.png"]    #nom des fichiers .png ...  objets utiles
checkpoint_names=["banane","drapeau","mur"]                  # nom des variables des images des objets utiles

back_fichier=["fond.jpg","mur_hauteur.jpg","mur_longueur.jpg"]
back_names=["fond","mur_hauteur","mur_longueur"]



x_screen=800  #taille horizontale de la fenetre
y_screen=600 # taille verticale de la fenetre

position_dk_X=x_screen/4            #Position de base, modifiable
position_dk_Y=y_screen/2

position_dk_X_2=x_screen*3/4        #Position de base J2
position_dk_Y_2=y_screen/2


qte_objet_lvl=[(2,4),(50,100),(100,200)]                                  # nombre d'ojbets a récolter en fonction du niveau
rect_menu=[(220,170,400,120),(220,320,400,120),(220,470,400,120)]                #position des boutons du menu

time_left_lvl=[1000*20,1000*50,1000*70]    #20,50 et 70 secondes de jeu

deplacements=[(-0.0125*x_screen,0),(0.0125*x_screen,0),(0,0.0166*y_screen),(0,-0.0166*y_screen)]  # HAUT BAS DROITE GAUCHE valeur des déplacements en X et Y




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~VARIABLES BINAIRES~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

var_menu=True   #Quand le jeu démarre, on est sur le menu, on a donc une condition vérifiée
var_jeu=False
actualise_once_menu=True
chrono_demarre=0   #pour l'instant le chrono n'est pas lancé
#---------------------------------------------#



"""A REGLER :
-CHRONO APRES APPUI SUR R
-Reinitialisation apres 3 fois "r"
-afficher 2 joueurs en meme temps
-amis ou ennemis ?"""





