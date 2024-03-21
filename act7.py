"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

#Daniela Ramos A01174259

from random import randrange
from turtle import *

from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Funcion que responde al toque de la pantalla
#Se cambiarion los valores de la velocidad de la pelota
def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 18
        speed.y = (y + 200) / 15

#Funcion que verifica si la pelota y targets se encuentra dentro de la pantalla
def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Funcion que dibuja la pelota y los objetivos
def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#Funcion que mueve la pelota y los objetivos
#Se cambio la velocidad de la pelota y los objetivos
def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.5

    if inside(ball):
        speed.y -= 1
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()