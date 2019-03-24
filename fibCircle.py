# coding making python 3.6
# fonte: https://trinket.io/python/43bc79b582
# -*- coding: utf-8 -*-

import turtle

# criação da janela e turtle
janela = turtle.Screen()
janela.bgcolor('black')
arte = turtle.Turtle()

# sequencia de fibonacci
n = 1
t = 0
s = 0
lista = []

while(n<=100):
    t = n
    n = n + s
    s = t
    lista.append(t)    

arte.goto(50,50)
arte.setheading(0)
arte.color('purple', 'red')

fator = 3

for i in range(len(lista)):
    arte.circle(-fator * lista[i], 90)

# to keep running
janela.exitonclick()