import turtle

# Configuração inicial
turtle.speed(2)
turtle.bgcolor("white")

# Desenhar o telhado
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.color("red")
turtle.begin_fill()
turtle.goto(0, 200)
turtle.goto(100, 100)
turtle.goto(-100, 100)
turtle.end_fill()

# Desenhar as paredes
turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(100, 100)
turtle.goto(-100, 100)
turtle.end_fill()

# Desenhar a porta
turtle.penup()
turtle.goto(-30, -100)
turtle.pendown()
turtle.color("brown")
turtle.begin_fill()
turtle.goto(-30, -40)
turtle.goto(30, -40)
turtle.goto(30, -100)
turtle.goto(-30, -100)
turtle.end_fill()

# Desenhar a janela
turtle.penup()
turtle.goto(40, 0)
turtle.pendown()
turtle.color("blue")
turtle.begin_fill()
turtle.goto(80, 0)
turtle.goto(80, 40)
turtle.goto(40, 40)
turtle.goto(40, 0)
turtle.end_fill()

# Desenhar o sol
turtle.penup()
turtle.goto(150, 150)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Desenhar a grama
turtle.penup()
turtle.goto(-250, -150)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.goto(250, -150)
turtle.goto(250, -250)
turtle.goto(-250, -250)
turtle.goto(-250, -150)
turtle.end_fill()

# Esconder a tartaruga
turtle.hideturtle()

# Manter a janela aberta
turtle.done()