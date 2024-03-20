#Jeannette A01236226
#Daniela Ramos A01174259
"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import *
from turtle import *


from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aimRandom = choice([vector(choice([-10, 10]), 0), vector(0, choice([-10, 10]))])

"""
Funcion que cambia la direccion de la serpiente
"""
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

"""
Funcion que determina si la cabeza de la serpiente se encuentra dentro
de los limites de la pantalla.
Devuelve verdadero si entra dentro de los limites
Devuelve falso si no
"""
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def insideFood(food):
    """Return True if food inside boundaries."""
    return -200 < food.x < 190 and -200 < food.y < 190


def moveFood():
    """Move food to a random direction one segment."""
    # Generar una nueva dirección aleatoria en cada llamada
    aimRandom = choice([vector(choice([-10, 10]), 0), vector(0, choice([-10, 10]))])

    food.move(aimRandom)
    #Verifica que la comida se encuentre dentro del recuadro
    if not insideFood(food):
        square(food.x, food.y, 0, 'red')
        update()
    #La comida se movera a la mitad de la velocidad que la serpiente
    ontimer(moveFood, 200) 
"""
Funcion que elige un color al azar de un arreglo de colores colorschoice
Se define el arreglo de 5 colores
Se devuelve un color al azar del arreglo con la funcion choice de la libreria random
"""
def changecolor():
    colorschoice=['orange','yellow','green','blue','purple']
    return choice(colorschoice)

"""
Funcion que define el movimiento de la serpiente
Se usa la funcion inside para verificar si la cabeza esta dentro de los limites
Se usa la funcion changecolor para cambiar el color de la serpiente y la comida al azar
"""
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    snakecolor=changecolor()

    for body in snake:
        square(body.x, body.y, 9, snakecolor)

    square(food.x, food.y, 9, changecolor())
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
