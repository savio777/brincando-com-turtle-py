# PYTHON TOPZERA

import turtle

janela = turtle.Screen()        # cria a janela
janela.bgcolor('black')         # cor do fundo da janela

savio = turtle.Turtle()         # nome da tartaruga
savio.color('green','red')      # cor da tartaruga
savio.pensize(5)                # tamanho da linha
savio.forward(150)              # tartaruga ir para frente 'n' unidades
savio.left(90)                  # tartaruga 'n' graus para a esquerda
savio.forward(150)              # desenha o segundo lado do triangulo
savio.left(45)
savio.forward(110)
savio.left(90)
savio.forward(110)
savio.left(45)
savio.forward(150)

bola = turtle.Turtle()          # outra tartaruga, metade de um circulo
bola.color('pink')
bola.heading()
bola.circle(120,180)
bola.color('purple')
bola.heading()
bola.circle(120,180)            # metade do circulo
bola.color('white')
bola.heading()
bola.circle(60)

janela.exitonclick()            # comando para a tela não fechar depois de executar