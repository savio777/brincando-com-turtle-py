# TENTAR FAZER CASA
# -*- coding: utf-8 -*-

import turtle

janela = turtle.Screen()
janela.bgcolor('pink')

seta = turtle.Turtle()
seta.color('black','red')
seta.forward(297) # chão da casa
# parede da direita
seta.left(90)
seta.forward(200)
# chaminé
seta.right(90)
seta.forward(20)
seta.left(135)
seta.forward(40)
seta.left(90)
seta.forward(40)
seta.left(135)
seta.forward(25)
seta.right(90)
seta.forward(40)
# teto
seta.right(90)
seta.forward(250)
seta.left(45)
seta.forward(50)
seta.left(135)
seta.forward(70)
seta.left(135)
seta.forward(50)
seta.left(90)
seta.forward(51)
seta.left(135) # aqui
seta.forward(299)
# porta e janelas
seta.right(90)
seta.forward(50)
seta.right(90)
seta.color('pink','red')
seta.forward(55)
seta.color('black','red')
seta.heading()          # primeira janela
seta.circle(15)
seta.color('pink','red')
seta.forward(65)
seta.color('black','red')
seta.heading()          # segunda janela
seta.circle(15)
seta.color('pink','red')
seta.forward(65)
seta.color('black','red')
seta.heading()          # terceira janela
seta.circle(15)
seta.color('pink','red')
seta.forward(42)  # talvez errado
seta.right(90)
seta.forward(50)
seta.color('black','red')
seta.forward(-125)
seta.left(90)
seta.forward(20)
seta.right(90)
seta.forward(80) # porta
seta.left(90)
seta.forward(28) # talvez errado
seta.left(90)
seta.forward(80)
seta.right(90)
seta.forward(25)
seta.right(90)
#parede da esquerda
seta.forward(130)

janela.exitonclick()
