# Daniela Ramos A01174259
# Jeannete Arjona A01236226
# Ángel Gael García Rangel A00833115 

"""
Catch Game

El juego consiste en letras cayendo desde el cielo, tu misión como jugador es atrapar las necesarias para formar la palabra indicada.

Tienes 5 vidas, cada letra atrapada que no sea la correspondiente a la palabra representará una vida menos.

"""

from random import *
import turtle
from freegames import vector
import time

# Define una lista para almacenar las letras atrapadas
letras_atrapadas = []
indicePalabra = 0
palabraGenerada = ""
vida = 5
flag = True

#Funcion para asignar una palabra
def palabra():
    global palabraGenerada
    palabra_pantalla = turtle.Turtle()  # Nueva tortuga para dibujar la palabra formada
    words = ['hola', 'arbol', 'cosa']
    selected_word = choice(words)  # Elegir una letra aleatoria de la lista
    palabraGenerada = selected_word
    palabra_pantalla.penup()
    palabra_pantalla.hideturtle()
    palabra_pantalla.goto(-100, 160)
    palabra_pantalla.color("black")
    palabra_pantalla.write(f"Palabra a formar: {''.join(selected_word)}", font=("Arial", 16, "bold"))


# Función para detectar colisiones entre dos objetos (canast y letra)
def detectar_colision(objeto1, objeto2):
    distancia = objeto1.distance(objeto2)
    if distancia < 20:  # Tamaño aproximado de la canasta
        return True
    else:
        return False
    
letras_pantalla = turtle.Turtle()  # Nueva tortuga para dibujar la palabra formada

#Función para actualizar el número de vidas restantes
def actualizar_vida():
    print(vida)
    letras_pantalla.clear()
    letras_pantalla.penup()
    letras_pantalla.hideturtle()
    letras_pantalla.goto(-100, 100)
    letras_pantalla.color("black")
    letras_pantalla.write((f"Vidas: {str(vida)}"), font=("Arial", 16, "bold"))
    
#Función para actualizar la subpalabra formada hasta el momento
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
    if vida == 0:
        letras_pantalla.penup()
        letras_pantalla.hideturtle()
        letras_pantalla.goto(-80, 0)
        letras_pantalla.color("black")
        letras_pantalla.write("Se han acabado tus vidas!", font=('Arial', 20, 'bold'))
        
# Función que representa el ciclo principal para generar las palabras que caen y para detectar colisiones entre canasta y letras.
def generate_falling_letters():
    global palabraGenerada, indicePalabra, vida, flag
    if vida > 0 and palabraGenerada != ''.join(letras_atrapadas):
        flag = True
    falling_pen = turtle.Turtle()  # Nueva tortuga para dibujar las letras que caen
    falling_pen.hideturtle()
    falling_pen.penup()

    letters = palabraGenerada

    while flag:
        actualizar_vida()
        letter = choice(letters)  # Elegir una letra aleatoria de la lista
        x = randint(-250, 250)  # Posición aleatoria en el eje x
        y = 200  # Empiezan desde arriba
        falling_pen.goto(x, y)
        falling_pen.write(letter, align="center", font=("Arial", 20, "normal"))

        # Hacer que la letra caiga gradualmente
        while y > -200:
            if vida <= 0 or palabraGenerada == ''.join(letras_atrapadas):  # Verificar si las vidas son 0
                flag = False  # Detener la generación de letras
                break
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
                else:
                    vida -= 1
                actualizar_letras_atrapadas()
                print("Letra atrapada:", letter)  # Imprimir la letra atrapada
                print("Letras atrapadas:", letras_atrapadas)  # Imprimir la lista de letras atrapadas
                break
                
            time.sleep(0.2)
        
        if palabraGenerada[indicePalabra] == letter:
            vida -= 1

            
        # Esperar antes de generar una nueva letra
        time.sleep(0.1)
        
#  Función para el dibujado de un rectángulo
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

# Incialización de la pantalla y el Turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightblue")  
pen = turtle.Turtle()
pen.speed(0) 

# Dibujar rectángulo
draw_rectangle(pen, "lightgreen", -300, -100, 600, 200)

# Dibujar sol
pen.penup()
pen.goto(200, 150)
pen.color("yellow")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

# Aignar la Turtle a la imagen "basket.gif"
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
#Generamos palabra a formar
palabra() 
#Generamos las letras cayendo 
screen.ontimer(generate_falling_letters, 1000)

screen.mainloop()


