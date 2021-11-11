# coding=utf-8
"""
Jeu de type "escape game". Projet informatique Château.
Auteurs : Fatima Kavak, Sacha Delsaux
N° matricules : 499353, 514349
Date : 15/11/2020
Jeu créé sur base d'un fichier texte représentant un labyrinthe dans lequel le joueur peut se déplacer
et répondre à des questions pour progresser jusqu'à la case finale.
Entrées : mouvements et réponses de l'utilisateur
Résultat : progression du personnage
"""
import turtle
from CONFIGS import *
turtle.setworldcoordinates(0,0,800,600) #déplace l'origine du système d'axes turtle en bas à gauche
turtle.speed(0)  #vitesse maximale turtle

LARGEUR = abs(ZONE_PLAN_MINI[0])+ abs(ZONE_PLAN_MAXI[0])
HAUTEUR = int((abs(ZONE_PLAN_MINI[1])+ abs(ZONE_PLAN_MAXI[1])))

def lire_matrice(fichier) :
    """"
    Lit un fichier texte et le met sous forme matrice
    entrée : fichier texte
    résultat : matrice du plan
    """
    with open(fichier) as fichier: #ouverture du fichier
        return [[int(colonne) for colonne in ligne.split()] for ligne in fichier] #le code lit chaque
    # ligne grâce à deux for imbriqués et les met sous forme de liste
matrice = lire_matrice(fichier_plan)

def calculer_pas(matrice):
    """"
      Cette fonction sert à déterminer la longueur du côté d'une case pour afficher le plan
      du château en entier
      entrée : la matrice du plan
      résultat : la longueur du côté d'une case pour afficher le plan en entier
      """
    a = LARGEUR/len(matrice[0])
    b = HAUTEUR/len(matrice)
    if a > b :
        return b #retourne la valeur minimale pour afficher le plan en entier
    else :
        return a #retourne la valeur minimale pour afficher le plan en entier
pas = calculer_pas(matrice)

def coordonnees (case, pas):
    """"
     cette fonction sert à déterminer les coordonnées d'une case déterminée par sa position en terme
     de ligne et colonne de la matrice.
     Entrée : case ( ligne et colonne), pas
     Résultat : retourne les coordonnées d'une case spécifique
     """
    ligne, colonne = case
    x,y = colonne*pas, HAUTEUR-pas-(pas*ligne) #les coordonnés en abssices sont représentées par la
    #position de la colonne * la longueur de la case. Les coordonnées en ordonnées sont représentées
    #par la hauteur - une longueur de case pour prendre le point inférieur gauche comme référence -
    #la position de la ligne* la longueur d'une case
    return x,y
dimension = pas
def tracer_carre(dimension):
    """"
     Cette fonction sert à dessiner un carré avec turtle.
       Entrée : la dimension du carré, c'est à dire la longueur de son côté
       Résultat : le dessin du carré
       """
    turtle.pendown()  #commande de début de traçage turtle
    for i in range(4):   #pour i de 1 à 4 (pour les côtés d'un carré)
        turtle.forward(dimension)   #avance de la longueur du côté
        turtle.left(90)  #tourne sur la gauche d'un angle droit
    turtle.penup()  #commande de fin de traçage turtle
    return
def tracer_case(case, couleur, pas):
    """
        Cette fonction sert à tracer une case d'une certaine couleur
        Entrée : la case (déterminée par sa position dans la matrice), une couleur (définie dans le fichier
        config selon sa valeur dans la matrice, pas ( la longueur du côté d'une case)
        """
    ligne, colonne = case
    couleur = COULEURS[matrice[ligne][colonne]] #la couleur est définie dans une liste du fichier config
    # la position ligne et colonne dans la matrice donne la valeur de la position dans la liste COULEURS
    #ce qui renvoie à une couleur spécifique selon la valeur dans la matrice
    turtle.penup()
    turtle.goto(coordonnees(case,pas)) #turtle va à la coordonné du sommet inférieur gauche de la case
    turtle.pendown()
    turtle.color(couleur)
    turtle.begin_fill()
    tracer_carre(dimension) #appel de la fonction qui permet de tracer un carré
    turtle.end_fill()
    return
def afficher_plan(matrice):
    """
    Cette fonction permet d'afficher le plan complet du château
    entrée : la matrice
    résultat : le plan du château affiché dans turtle
    """
    for ligne in range(len(matrice)): #le code lit chaque ligne de la matrice
        for colonne in range(len(matrice[0])): #le code lit chaque colonne de la matrice
            tracer_case((ligne,colonne),COULEURS, pas)  #appelle la fonction qui permet de tracer la
            #case correspondante de position ligne et colonne spécifique
    return
def afficher_annonces():
    """
    Cette fonction permet de définir la zone d'annonce des évenements. Il suffira par la suite de
    l'appeler pour effacer les annonces précédentes
    """
    turtle.penup()
    turtle.goto((0,500))
    turtle.pendown()
    turtle.color("White")
    turtle.setheading(0)
    turtle.forward(600)
    turtle.setheading(90)
    turtle.forward(100)
    turtle.setheading(180)
    turtle.forward(600)
    turtle.setheading(270)
    turtle.forward(100)
    turtle.penup()

afficher_plan(matrice)
def creer_dictionnaire_des_objets(fichier_objets,fichier_questions):
    """
       Cette fonction permet de créer un dictionnaire depuis les fichiers dico_objets et dico_portes
       Entrée : fichier_objets, fichier_questions
       Sortie : dictionnaire contenant les indices et les questions
       """
    s={} #crée un dictionnaire
    for ligne in open(fichier_objets,encoding='utf-8'): #lit chaque ligne du fichier_objet
        a,b = eval(ligne) #attribue à a les coordonnées et b l'élément second du tuple
        s.update({a:b}) #ajoute ses éléments sous forme dictionnaire
    for ligne2 in open(fichier_questions,encoding='utf-8'):
        c,d = eval(ligne2) #attribue à c les coordonnées et d l'élément second du tuple
        s.update(({c:d})) #ajoute ses éléments sous forme dictionnaire
    return s
nom_objet = creer_dictionnaire_des_objets(fichier_objets,fichier_questions)
a=0
def deplacer_haut():
    """Créer une fonction déplcer_haut qui va faire avancer le personnage en haut, si le joueur utilise
             la flèche haut
             Entrée : cette fonction n'utilise pas de paramètre
             Résultats : déplacement d'une case vers le haut"""
    global matrice,x,y, mouvement    #paramètre global
    mouvement = (0,-1)               #mouvement lorsque personne monte
    if y ==0:
        None
    else:
        if matrice[y-1][x] != 1:    #si la prochaine case en haut n'est pas un mur, condition vérifiée
            y -= 1                   #modifier la coordonnee y, prend en compte le déplacement vers le haut
            if matrice[y][x] == 3:  #si la prochaine case en haut est une porte, condition vérifiée
                poser_question(matrice,mouvement)  #appelle la fonction poser_question définie plus loin
            elif matrice[y][x] == 4:    #si la prochaine case en haut est un objet, condition vérifiée
                turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y)) #le personage a avancé sur la case où se
                                                                           #trouve l'objet
                ramasser_objet(matrice)  #appelle fonction ramasser_objet définie plus loin
            else:
                turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))  #si la prochaine case en bas est une case
            #blanche, avancez normalement

def deplacer_bas():
    """Créer une fonction déplcer_bas qui va faire avancer le personnage vers le bas si le joueur utilise
            la flèche du bas
            Entrée : cette fonction n'utilise pas de paramètre
            Résultats : déplacement d'une case vers le bas"""
    global matrice,x,y,mouvement #parametre global
    mouvement = (0,1)             #mouvement lorsque personne descend
    if y ==len(matrice)-1:
        None
    else :
        if matrice[y+1][x] != 1:  #si la prochaine case en bas n'est pas un mur, condition vérifiée
            y += 1                  #modifier la coordonnee y, prend en compte le déplacement vers le bas
            if matrice[y][x] == 3:  #si la prochaine case en bas est une porte, condition vérifiée
                poser_question(matrice,mouvement)   #appelle la fonction poser_question
            elif matrice[y][x] == 4:     #si la prochaine case en bas est un objet, condition vérifiée
                turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y)) #le personage a avancé sur la case où se
                                                                           #trouve l'objet
                ramasser_objet(matrice)   #appelle la fonction ramasser_objet
            else:
                turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y)) #si la prochaine case en bas est une case
            #blanche, avancez normalement
def deplacer_gauche():
    """Créer une fonction déplcer_droite qui va faire avancer le personnage à gauche, si le joueur utilise
           la flèche gauche
           Entrée : cette fonction n'utilise pas de paramètre
           Résultats : déplacement d'une case vers la gauche """
    global matrice,x,y,mouvement   #parametre global
    mouvement =(-1,0)               #mouvement lorsque va à gauche
    if matrice[y][x-1] != 1:          #si la prochaine case à gauche n'est pas un mur, condition vérifiée
        x -= 1                         #modifier la coordonnee x, prend en compte le déplacement vers la gauche
        if matrice[y][x] == 3:        #si la prochaine case à gauche est une porte, condition vérifiée
            poser_question(matrice,mouvement)  #appelle la fonction poser_question
        elif matrice[y][x] == 4:               #si la prochaine case à gauche est un objet, condition vérifiée
            turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y)) #le personage a avancé sur la case où se
                                                                           #trouve l'objet
            ramasser_objet(matrice)  #appelle la fonction ramasser_objet
        else:
            turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y)) #si la prochaine case en bas est une case
            #blanche, avancez normalement
def deplacer_droite():
    """Créer une fonction déplcer_droite qui va faire avancer le personnage à droite, si le joueur utilise
    la flèche droite
    Entrée : cette fonction n'utilise pas de paramètre
    Résultats : déplacement d'une case vers la droite
    """
    global matrice,x,y,mouvement  #parametre global
    mouvement=(1,0)               #mouvement lorsque va à droite
    if matrice[y][x+1] !=1:      #si la prochaine case à droite n'est pas un mur, condition vérifiée
        x += 1                    #modifier la coordonnee x, prend en compte le déplacement vers la droite
        if matrice[y][x] == 3:    #si la prochaine case à droite est une porte, condition vérifiée
            poser_question(matrice,mouvement)   #appelle la fonction poser_question
        elif matrice[y][x] == 4:     #si la prochaine case à droite est un objet, condition vérifiée
            turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))   #le personage a avancé sur la case où se
                                                                           #trouve l'objet
            ramasser_objet(matrice)      #appelle la fonction ramasser_objet
        else:
            turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))  #si la prochaine case en bas est une case
            #blanche, avancez normalement
def deplacer(matrice,position):
    """Crée une fonction déplacer qui va gérer les déplacements du personnage et associer à une flèche du clavier,
         un déplacement.
         Entrée : matrice, position
         Résultats : Pouvoir se déplacer """
    global x,y       #parametre global
    x,y = position
    turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))    #le personnage va à la case de départ
    while matrice[y][x] !=2:            #tant que le joueur n'a pas atteint la case finale, la boucle s'éxecute
        turtle.shape("circle")          #transformer le curseur en cercle
        turtle.shapesize(0.5)           #modifier la taille du curseur
        turtle.color("Red")             #modifier la couleur du curseur à rouge
        turtle.listen()                   #instruction turtle pour pouvoir gérer les déplacements
        turtle.onkeypress(deplacer_haut, "Up")  #Quand flèche haut pressée, appelle la fonction deplacer_haut
        turtle.onkeypress(deplacer_bas, "Down")  #Quand flèche bas pressée, appelle la fonction deplacer_bas
        turtle.onkeypress(deplacer_gauche, "Left")   #Quand flèche gauche pressée, appelle la fonction deplacer_gauche
        turtle.onkeypress(deplacer_droite, "Right")    #Quand flèche droite pressée, appelle la fonction deplacer_droite
        turtle.mainloop()
    turtle.hideturtle()
    turtle.color("White")
    turtle.begin_fill()
    afficher_annonces()
    turtle.end_fill()
    turtle.color("Red")
    turtle.setpos(50, 550)
    turtle.write("Vous avez gagné !")
def ramasser_objet(matrice):
    """Créer une fonction ramasser_objet qui, lorsque le personne se situe sur une case verte, collecte l'objet qui
        s'y trouve, affiche  et l'ajoute dans l'inventaire. Ces objets sont des indices qui aideront à répondre aux
        questions de la fonction poser_question
        Entree : matrice
        Résultats : transformation de la case objet en case couloir, ajout de l'objet dans l'inventaire """
    turtle.color("White") #changer couleur blanc pour transformer l'objet en case blanche
    turtle.penup()
    turtle.setheading(180) # changer la direction du curseur vers la gauche
    turtle.forward(pas//2) # avancer de pas//2, afin de déplacer le curseur du milieu vers la gauche
    turtle.setheading(270) # changer la direction du curseur vers le haut
    turtle.forward(pas//2) # avancer de pas//2, afin de déplacer le curseur du milieu gauche, au coin supérieur gauche
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    tracer_carre(pas)
    turtle.end_fill()
    global a
    a -= 15
    turtle.hideturtle() #cacher le curseur
    turtle.color("White")
    turtle.begin_fill()
    afficher_annonces()
    turtle.end_fill()
    turtle.color("Red")
    turtle.setpos(50,550) #définir la position de l'affichage d'annonces
    turtle.write("Vous avez trouvé : ") #écrire un message dans l'affichage d'annonces
    turtle.setpos(250,550)
    turtle.write(nom_objet[(y,x)])  #ecrire un autre message dans l'affichage d'annonces
    turtle.setpos(400,420)          #définir la position de l'inventaire
    turtle.write("Inventaire :")    #ecrire "Inventaire" dans l'affichage d'inventaire
    turtle.setpos(400,400+a)
    turtle.write(nom_objet[(y,x)]) #ecrire dans l'inventaire les objets collectionnés
    turtle.showturtle()
    turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))
    matrice[y][x] = 0             #transformer la valeur de la matrice de l'objet en 0
def poser_question(matrice,mouvement):
    """Creer une fonction poser_questions qui, lorsque le personnage voudra se rendre sur une case jaune, lui posera une
      question. Si la réponse est correcte, elle se déplacera sur cette case et la transformera en case_couloir.
      Entree : matrice, mouvement
      Résultats :  """
    global x,y
    s,t = mouvement            #assigner 2 variables au tuple mouvement
    a,b = nom_objet[(y,x)]     #assiner la variable a à la question et la variable b à la reponse attendue
    turtle.hideturtle()
    turtle.color("White")
    turtle.begin_fill()
    afficher_annonces()
    turtle.end_fill()
    turtle.color("Red")
    turtle.setpos(50, 550)    #définir position de l'affichage d'annonces
    turtle.write("Cette porte est fermée !")  #imprimer texte dans l'affichage d'annonces
    if turtle.textinput("Question",a) == b:   #si la reponse donnee par le joueur est correcte alors executer le code
        turtle.showturtle()
        turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))   #avance sur la case questions
        matrice[y][x] = 0                                                #transforme la valeur de la matrice a 0
        turtle.hideturtle()
        turtle.color("White") #changer la couleur de la case en blanc
        turtle.penup()
        turtle.setheading(180)
        turtle.forward(pas // 2)
        turtle.setheading(270)
        turtle.forward(pas // 2)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        tracer_carre(pas)   #retracer un carre blanc à l'emplacement de l'objet
        turtle.end_fill()
        turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))
        turtle.showturtle()
        turtle.color("Red")
    else:                   #si le joueur n'a pas bien répondu à la question
        turtle.showturtle()
        x = x-s             #incrémenter ou décrémenter la position de x par l'inverse du mouvement déjà enregistrée
        y =y-t               #incrémenter ou décrémenter la position de y par l'inverse du mouvement déjà enregistrée
        turtle.goto(x * pas + pas / 2, HAUTEUR - pas / 2 - (pas * y))   #retourner à la case avant la porte
    turtle.listen()
afficher_annonces()
deplacer(matrice,(1,0))
