"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

#Importa librerías
from random import randrange
from turtle import *
from freegames import vector
#Crea dos vectores y una lista vacía
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Función que se activa cuando el usuario hace click
def tap(x, y):
    """Respond to screen tap."""
    #Verifica si la pelota se encuentra o no dentro de la pantalla
    if not inside(ball):
        #Si no está, coloca la pelota en posición iniciial
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 20
        speed.y = (y + 200) / 20

#Función que devuelve False/True si el objeto está dentro de la pantalla
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Función que dibuja las figuras del juego
def draw():
    """Draw ball and targets."""
    clear()
    #Dibuja los círculos azules
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
    
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
    #Actualiza la pantalla
    update()

#Función que mueve las figuras en la pantalla
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)
    #Crea una copia de la lista "targets"
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
    #Actualiza la pantalla
    draw()
    #Temporizador que llama a la función "move" de nuevo
    ontimer(move, 15)

#Define las dimensiones de la ventana de juego
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()