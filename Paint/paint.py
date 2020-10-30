from turtle import *
from freegames import vector
import math #Librería para cálculos matemáticos

#Elaborado por:
"""Salvador Alejandro Gaytán Ibañez A01730311
Ituriel Mejia Garita A01730875
Myroslava Sánchez Andrade A01730712
Víctor Alfonso Mancera Osorio A01733749"""

#Función que dibuja una línea
def line(start, end):
    up() #Levantar lápiz (no dibujar)
    goto(start.x, start.y) #Ir a coordenada del primer punto
    down() #Bajar lápiz (empezar a dibujar)
    goto(end.x, end.y) #Ir a segundo punto

#Función que dibuja un cuadrado
def square(start, end):
    up() #Levantar lápiz (no dibujar)
    goto(start.x, start.y) #Ir a coordenada del primer punto
    down() #Bajar lápiz (empezar a dibujar)
    begin_fill() #Establecemos que se rellenará la figura

    #Ciclo que traslada el lápiz a cada uno de los puntos
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill() #  #Finalizamos el llenado

#Función que dibuja un circulo, el primer punto es el centro y el segundo cualquier punto de la circunferencia
def circlee(start, end):
    r=math.sqrt(((end.x-start.x)**2)+((end.y-start.y)**2)) #Calcular radio
    up() #Levantar lápiz (no dibujar)
    goto(start.x, (start.y-r)) #Ir al punto más bajo de la circunferencia (desde ahi empieza a dibujar circle)
    down() #Bajar lápiz (empezar a dibujar)
    begin_fill()#Establecemos que se rellenará la figura
    circle(r) #Se dibuja círculo de radio r
    end_fill()  #Finalizamos el llenado

#Función que dibuja un rectángulo. Los dos puntos dados son dos de sus esquinas
def rectangle(start, end):
    up() #Levantar lápiz (no dibujar)
    goto(start.x, start.y) #Ir a coordenada del primer punto
    down() #Bajar lápiz (empezar a dibujar)
    begin_fill() #Establecemos que se rellenará la figura

    #Se recorren los cuatro vértices del rectángulo
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

#Guarda información de coordenadas cuando se da click en el canvas
def tap(x, y):
    start = state['start']

    #Si el start es None, se guarda en el la información del click
    if start is None:
        state['start'] = vector(x, y)
    #Si no, entonces se dibuja la figura, siendo el click la información de end. Al final start se reestablece
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Guarda el tipo de figuras que se están dibujando
def store(key, value):
    state[key] = value

state = {'start': None, 'shape': line} #Valores iniciales. Se empieza con linea por default
setup(420, 420, 370, 0) #Medidas del canva
onscreenclick(tap) #Llama función tap en cada click
listen()
onkey(undo, 'u') #Deshacer cuando se presione 'u'

#Cambio de colores cuando se presionen las teclas señaladas
onkey(lambda: color('black'), 'K') 
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

#Cambio de figura cuando se presionen las teclas señaladas (se llama store para guardar este valor)
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circlee), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done() #Determina el loop para esperar instrucciones en pantalla