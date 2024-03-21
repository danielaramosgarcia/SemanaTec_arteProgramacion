# Daniela Ramos A01174259
# Jeannete 
# Gael 

"""
Catch Game

This is a game where letters fall from the top of the screen and the player needs to catch them to form words.

The objective of the game is to catch as many letters as possible and create as many words as you can within a given time limit.

Enjoy the challenge and have fun playing!

"""

from random import *
import turtle
from freegames import vector
import time

#Daniela Ramos A01174259


# Define una lista para almacenar las letras atrapadas
letras_atrapadas = []
indicePalabra = 0
palabraGenerada = ""
#Funcion para asignar una palabra
def palabra():
    global palabraGenerada
    palabra_pantalla = turtle.Turtle()  # Nueva tortuga para dibujar la palabra formada
    words = ['parque', 'manzana', 'amarillo']
    selected_word = choice(words)  # Elegir una letra aleatoria de la lista
    palabraGenerada = selected_word
    palabra_pantalla.penup()
    palabra_pantalla.hideturtle()
    palabra_pantalla.goto(-100, 160)
    palabra_pantalla.color("black")
    palabra_pantalla.write(f"Palabra a formar: {''.join(selected_word)}", font=("Arial", 16, "bold"))

# Función para detectar colisiones entre dos objetos
def detectar_colision(objeto1, objeto2):
    distancia = objeto1.distance(objeto2)
    if distancia < 20:  # Tamaño aproximado de la canasta
        return True
    else:
        return False
    
    
def actualizar_letras_atrapadas():
    letras_pantalla = turtle.Turtle()  # Nueva tortuga para dibujar la palabra formada
    letras_pantalla.undo()  # Deshacer el texto anterior
    letras_pantalla.penup()
    letras_pantalla.hideturtle()
    letras_pantalla.goto(-100, 120)
    letras_pantalla.color("black")
    letras_pantalla.write(f"Palabra formada: {''.join(letras_atrapadas)}", font=("Arial", 16, "bold"))
    if(palabraGenerada== ''.join(letras_atrapadas)):
        letras_pantalla.penup()
        letras_pantalla.hideturtle()
        letras_pantalla.goto(-80, 0)
        letras_pantalla.color("black")
        letras_pantalla.write("¡Ganaste!", font=('Arial', 20, 'bold'))
    

# Función para generar letras que caen
def generate_falling_letters():
    global palabraGenerada, indicePalabra
    falling_pen = turtle.Turtle()  # Nueva tortuga para dibujar las letras que caen
    falling_pen.hideturtle()
    falling_pen.penup()

    letters = palabraGenerada

    while True:
        letter = choice(letters)  # Elegir una letra aleatoria de la lista
        x = randint(-250, 250)  # Posición aleatoria en el eje x
        y = 200  # Empiezan desde arriba
        falling_pen.goto(x, y)
        falling_pen.write(letter, align="center", font=("Arial", 20, "normal"))

        # Hacer que la letra caiga gradualmente
        while y > -200:
            y -= 9  # Mover hacia abajo
            falling_pen.clear()  # Borrar la letra anterior
            falling_pen.goto(x, y)  # Mover a la nueva posición
            falling_pen.write(letter, align="center", font=("Arial", 20, "normal"))
            screen.update()  # Actualizar la pantalla manualmente
            
            # Detectar colisión con la canasta
            if detectar_colision(falling_pen, pen):
                falling_pen.clear()  # Borrar la letra atrapada
                if palabraGenerada[indicePalabra] == letter:
                    letras_atrapadas.append(letter)  # Agregar la letra atrapada a la lista
                    indicePalabra += 1
                    actualizar_letras_atrapadas()
                print("Letra atrapada:", letter)  # Imprimir la letra atrapada
                print("Letras atrapadas:", letras_atrapadas)  # Imprimir la lista de letras atrapadas
                break
                
            time.sleep(0.2)
            
        # Esperar antes de generar una nueva letra
        time.sleep(0.1)
# Function to draw a rectangle
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Initialize the screen and turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")  # Set sky color
pen = turtle.Turtle()
pen.speed(0)  # Set drawing speed to fastest



# Draw grass
draw_rectangle(pen, "lightgreen", -300, -100, 600, 200)

# Draw sun
pen.penup()
pen.goto(200, 150)
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()


# Set the shape of the turtle to the image "basket.gif"
positon = vector(0, -50)
pen.goto(positon.x, positon.y)
screen.addshape("basket.gif")
pen.shape("basket.gif")

turtle.listen()

def move_right():
    positon.x += 10
    pen.goto(positon.x, positon.y)

def move_left():
    positon.x -= 10
    pen.goto(positon.x, positon.y)

turtle.onkey(move_right, 'Right')
turtle.onkey(move_left, 'Left')

pen.penup()
#Generar palabra a formar
palabra()
#Generar letras 
screen.ontimer(generate_falling_letters, 1000)

screen.mainloop()


