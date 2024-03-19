
#Daniela Ramos A01174259
#Gael Garcia A00833115
#Jaennette A01236226


"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

"""
Funcion que dibuja visualmente una linea desde el punto de inicio hasta el punto final
Se usa la funcion up() para levantar el lapiz y no dejar rastro de la linea mientras se posiciona
Se usa la funcion goto() para mover el lapiz a la posicion de inicio
Se usa la funcion down() para bajar el lapiz y dejar rastro de la linea mientras se dibuja
Se usa la funcion goto() para mover el lapiz a la posicion final
"""
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

"""
Funcion que dibuja visualmente un cuadrado desde el punto de inicio hasta el punto final
Se usa la funcion up() para levantar el lapiz y no dejar rastro de la linea mientras se posiciona
Se usa la funcion goto() para mover el lapiz a la posicion de inicio
Se usa la funcion down() para bajar el lapiz y dejar rastro de la linea mientras se dibuja
Se usa la funcion begin_fill() para empezar a rellenar la figura
Se usa la funcion forward() para mover el lapiz hacia adelante la distancia entre el punto de inicio y el punto final
"""
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

"""
Funcion que dibuja visualmente un circulo desde el punto de inicio hasta el punto final
Se usa la funcion up() para levantar el lapiz y no dejar rastro de la linea mientras se posiciona
Se usa la funcion goto() para mover el lapiz a la posicion de inicio
Se usa la funcion down() para bajar el lapiz y dejar rastro de la linea mientras se dibuja
Se usa la funcion begin_fill() para empezar a rellenar la figura
Se usa la funcion circle() para dibujar un circulo con un radio de 50
"""
def draw_circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    circle(50)
    end_fill()


"""
Funcion que dibuja visualmente un rectangulo desde el punto de inicio hasta el punto final
Se usa la funcion up() para levantar el lapiz y no dejar rastro de la linea mientras se posiciona
Se usa la funcion goto() para mover el lapiz a la posicion de inicio
Se usa la funcion down() para bajar el lapiz y dejar rastro de la linea mientras se dibuja
Se usa la funcion begin_fill() para empezar a rellenar la figura
Se usa la funcion forward() para mover el lapiz hacia adelante la distancia entre el punto de inicio y el punto final
Se usa la funcion left() para girar el lapiz 90 grados a la izquierda
Se usa la funcion end_fill() para dejar de rellenar la figura
"""
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    initialDistance = end.x - start.x
    smallerDistance = initialDistance * 0.7
    flag = True
    for count in range(4):
        if flag:
            forward(initialDistance)
            flag = False
        else:
            forward(smallerDistance)
            flag = True
        left(90)
    end_fill()

"""
Funcion que dibuja visualmente un triangulo desde el punto de inicio hasta el punto final
Se usa la funcion up() para levantar el lapiz y no dejar rastro de la linea mientras se posiciona
Se usa la funcion goto() para mover el lapiz a la posicion de inicio
Se usa la funcion down() para bajar el lapiz y dejar rastro de la linea mientras se dibuja
Se usa la funcion begin_fill() para empezar a rellenar la figura
Se usa la funcion forward() para mover el lapiz hacia adelante la distancia entre el punto de inicio y el punto final
Se usa la funcion left() para girar el lapiz 120 grados a la izquierda
"""
def triangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()
    
"""
Funcion que deshace el ultimo movimiento del lapiz
"""
def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

"""
Funcion que cambia el color de la linea y el relleno de la figura
"""
def store(key, value):
    """Store value in state at key."""
    state[key] = value

"""
Parte del codigo que se encarga de cambiar el color de la linea y el relleno de la figura segun la tecla presionada
"""

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
#added red line filled with pink color when pressed the letter P
onkey(lambda: color('red','pink'), 'P')
onkey(lambda: store('shape', line), 'l')	
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()