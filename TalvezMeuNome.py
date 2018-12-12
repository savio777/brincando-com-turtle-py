# -*- coding: utf-8 -*-
'''ninguem liga'''

import turtle

janela = turtle.Screen()
janela.bgcolor('black')

queTedio = turtle.Turtle()
# S
queTedio.color('black','red')
queTedio.right(90)
queTedio.forward(250) # para baixo
queTedio.color('green','red')
queTedio.right(90)
queTedio.forward(100)
queTedio.right(90)
queTedio.forward(100)
queTedio.forward(-100)
queTedio.right(90)
queTedio.forward(100)
queTedio.left(90)
queTedio.forward(100)
queTedio.right(90)
queTedio.forward(100)
queTedio.right(90)
queTedio.forward(100)
# A
queTedio.forward(-100)
queTedio.left(180)
queTedio.color('black','red')
queTedio.forward(50) # espaço entre uma letra e outra
queTedio.color('green','red')
queTedio.left(90)
queTedio.forward(200)
queTedio.right(90)
queTedio.forward(100)
queTedio.forward(-100)
queTedio.right(90)
queTedio.forward(100)
queTedio.left(90)
queTedio.forward(100)
queTedio.right(90)
queTedio.forward(100)
queTedio.forward(-200)
# V
queTedio.left(90)
queTedio.color('black','red')
queTedio.forward(50) # espaço entre o a e o v
queTedio.color('green','red')
queTedio.right(75)  # angulo da metade do v
queTedio.forward(200)
queTedio.right(200) # angulo da outra metade do v
queTedio.forward(200)
# I
queTedio.color('black','red')
queTedio.right(90)
queTedio.forward(25)  # espaço entre o v e o i
queTedio.color('green','red')
queTedio.right(90)
queTedio.forward(200)

janela.exitonclick()
