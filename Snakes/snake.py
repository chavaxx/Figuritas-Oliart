

from turtle import *
from random import randrange
from freegames import square, vector

#Elaborado por:
"""Salvador Alejandro Gaytán Ibañez A01730311
Ituriel Mejia Garita A01730875
Myroslava Sánchez Andrade A01730712
Víctor Alfonso Mancera Osorio A01733749"""

#Establecemos el vector que contiene la posiciones de comida al igual que la de snake, y la de la dirección d
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#Creamois un arreglo con los colores disponibles tanto para la serpiente como para la comdia
colores = ["green", "red", "yellow", "black", "blue"]
#Establecemos que el color serpiente y colorCOmida seráa un color al azar, de acuerdo a un valor numerico al azar en tr0 y 4
colorSerpiente = colores[randrange(5)]
colorComida = colores[randrange(5)]

#Funcion que se encarga de cambiar la direccion de la serpiente
def change(x, y):

    print("Andamos cambiando lmao")
    aim.x = x
    aim.y = y

def change_food(x, y): #Funcion que se encarga de cambiar la posicion de la comida de acuerdo a los argumentos provistos
    print("Cambiando la posición de la comida")
    #Asignamos los componentes vectoriales de mi vector comida a lo que se nos brinde como argumento
    food.x = x
    food.y = y


def inside(head): #Funcion que nos indica si la serpiente se encuentra en los boundaries
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy() #Accedemos al ultimo cuadro de la serpiente (El cual es la cabeza)
    head.move(aim) #Lo movemos hacia el aim

    if not inside(head) or head in snake: #Si nuestra serpiente se sale de sus boundaries...
        square(head.x, head.y, 9, 'red') #Establecemos la cabeza como un cuadro rojo
        update() #Actualizamos el canvas
        return #Regresamos

    snake.append(head) #Añadimos a nuestra snake la cabeza

    if head == food: #Si la cabeza se encuentra en el mismo lugar de la comdia
        print('Snake:', len(snake)) #Imprimimos que se han encontrado
        # Colocamos la comida en un valor al azar
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else: #De cualquier otra forma, eliminamos la cola de la serpíente parta simular el movimiento
        snake.pop(0)

    clear() #Limpiamos el canvas

    for body in snake: #Construimos de nueva cuenta el snake
        square(body.x, body.y, 9, colorSerpiente)

    numero = randrange(1, 10) #Obtenemos una variable de numero al azar entre 1 y 10
    if numero == 5: #Si ese numero es 5...
        change_food(randrange(1,5)*10, randrange(1, 6)*10) #Cambiamos la posicion de la comida a un valor al azar
        while(not inside(food)): #Evaluamos que este dentro de los limites del canvas
            #Si no lo está, volvemos a reubicarla hasta que esté dentro de los limites
            change_food(randrange(0, 5) * 10, randrange(0, 6) * 10)
    #Finalmente dibujamos la comida
    square(food.x, food.y, 9, colorComida)


    #Actualizamos el canvas
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0) #Establecemos el tamaño de la venta
hideturtle() #Esondemos la tortuga que dibuja
tracer(False) #Eliminamos el tracer del dibujo
listen() #Estableces un escucha que esta atento a las instrucciones del usuario

#Serie listeners que se encargan de ejecutar una funcion de acuerdo a la tecla preisonada
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
#Ejecutamos la funcion mover
move()
#Establecemos que hasta aquí llega el ciclo del programa
done()