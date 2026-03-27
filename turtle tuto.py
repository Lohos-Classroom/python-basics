## importer les fonctions de dessin de la librairie turtle
## from turtle import *

## dessiner de 100 pixels vers l'avant
## forward(100)

## s'orienter dans le sens horraire (vers la droite) de 90 degrés
## right(90)

## pour connaitre la position de la tortue qui dessine
## (utile pour verifier les distances a faire si besoin)
## print ("x : ", pos()[0])
## print ("y : ", pos()[1])

## Maintenant c'est a vous, desactivez les lignes du tuto en mettant ## devant
## ne desactivez la ligne from turtle import *
## ou reecriver la en dessous si vous le faite







## etoile qui se multiplie en cercle
from turtle import *

## pour aller vite
speed(0)
tracer(0)

## fonction pour faire l'etoile
def etoile(angle_etoile, taille_etoile) :
    for i in range(5) :
        right(angle_etoile)
        forward(taille_etoile)

## se mettre en postition
up()
forward(100)
down()

## repeter l'etoile mais en la decalant un peu a chaque fois
for i in range(360) :
    etoile(144, 200)
    right(1)
    update()

## fermer la fenetre avec echap
listen()
onkey(bye, "Escape")
done()

