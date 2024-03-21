letras_pantalla = turtle.Turtle()  # Nueva tortuga para dibujar la palabra formada
    letras_pantalla.undo()
    letras_pantalla.penup()
    letras_pantalla.hideturtle()
    letras_pantalla.goto(-100, 100)
    letras_pantalla.color("black")
    letras_pantalla.write(("Vidas: " + str(vida)), font=("Arial", 16, "bold"))
    