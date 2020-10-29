from turtle import *
from freegames import vector
import math

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circlee(start, end):
    "Draw circle from start to end."
    r=math.sqrt(((end.x-start.x)**2)+((end.y-start.y)**2))
    up()
    goto(start.x, (start.y-r))
    down()
    begin_fill()
    circle(r)
    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    goto(start.x,end.y)
    goto(end.x,end.y)
    goto(end.x,start.y)
    goto(start.x, start.y)    
    
    end_fill() #Finalizamos el llenado

def triangle(start, end):
    up() #Alzamos el pincel (Es decir, dejamos de dibujar)
    goto(start.x, start.y) #Ubicamos el pincel en la ubicación que selecciona el usario con su mouse
    down() #Lo colocamos en el canvas
    begin_fill() #Establecemos que se rellenará la figura

    goto(end.x,end.y) ##Iremos a la posición del segundo punto dado
    goto(end.x,start.y) #Permanecerá en la coordenada x del segundo punto, pero irá a la coordenada Y del primero
    goto(start.x, start.y) #Regresar a las coordenadas del primer punto

    end_fill() #Finalizamos el llenado


def tap(x, y):
    "Store starting point or draw shape."

    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

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
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circlee), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()