"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

#Daniela Ramos Garcia A01174259
#Ángel Gael García Rangel A00833115
#Jeannette Arjona Hernandez A01236226
""" 
Instrucciones:
Antes de comenzar el juego, la línea de comandos te preguntará si quieres usar letras o números. 
Una vez que coloques qué tipo de dato quieres usar, el juego comenzará.
Encuentra los 32 pares pafra desbloquear la imagen.
"""
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tab_count = 0
onLetters = False
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tab_count
    tab_count += 1
    print(f"Tab count: {tab_count}")

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

#Se modifico la ubicacion de los numeros al dar tab para que se vean centrados
def draw():
    """Draw image, tiles, and tab count."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        if onLetters:
            goto(x, y + 7)
        else:
            if tiles[mark] < 10:
                center = 17  # Center single-digit numbers
            else:
                center = 10  # Center two-digit numbers
            goto(x + center, y + 7)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display tab count
    up()
    goto(-50, 200)  # Adjust the coordinates as needed
    color('pink')
    down()
    write(f"Tab count: {tab_count}", font=('Arial', 20, 'bold'))

    update()
    
    # Verificar si ya se acabaron las tabs
    if all(not item for item in hide):
        up()
        goto(-80, 0)
        color('yellow')
        down()
        write("¡Ganaste!", font=('Arial', 20, 'bold'))
        update()
        
    ontimer(draw, 100)

option = input("If you want to use letters write L, write any other letter to use numbers: ")
if option == "L":
    tiles = ['cat', 'dog', 'hat', 'car', 'run', 'fun', 'sun', 'red', 'big', 'pen', 
                'cup', 'top', 'cup', 'box', 'boy', 'toy', 'sky', 'jam', 'mix', 'hot', 
                'man', 'pet', 'mat', 'mad', 'zip', 'dip', 'map', 'bat', 'leg', 'pig', 'rug', 'lup'] * 2
    onLetters = True
shuffle(tiles)
setup(480, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()