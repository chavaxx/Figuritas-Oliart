"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

#Agregamos librerías
from random import *
from turtle import *
from freegames import path

#Se declara la imagen
car = path('car.gif')
#Creamos nuestro tablero
tiles = list(range(32)) * 2
state = {'mark': None}
#Se inicializa el tablero con las fichas escondidas
hide = [True] * 64
numTaps=0
tapsDestapados=0

#Función que dibuja los cuadros
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Se convierten las coordinadas en los índices de cada tile
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Se convierte cada tile contado en una coordenada
#Es decir que a cada cuadrito se le asigna una coordenada
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Creamos la función que imprime el número de taps
def printTaps():
    global numTaps
    #Se le va sumando uno
    numTaps=numTaps+1
    print("Number of taps: "+str(numTaps))

#Función que verfifica si ha terminado de destapar todos los cuadros
def terminado():
    global tapsDestapados
    tapsDestapados=tapsDestapados+1

    #Cuando se termine se imprime en pantalla el mensaje
    if(tapsDestapados==32):
        print("Todos los cuadros se han destapado :D")

'''Función que actualiza la marca y el estado de la tile 
(!hidden o hidden) dependiendo del tap'''
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']
    
    #En caso de que las tiles no tengan la misma marca, se dejan escondidas
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    #Si tienen la misma marca, se enseña la parte de a imagen de los tailes
    else:
        hide[spot] = False
        hide[mark] = False
        #Se le quita la marca
        state['mark'] = None
        #Se llama a la función terminado para verificar si ya se ha terminado el juego
        terminado()
    #Llamamos a la función printTaps para que imprima los taps
    printTaps()

#Función que dibuja los tiles de la imagen
def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    #Se define su mark con la que ya tiene
    mark = state['mark']
    
    #En caso de no tener marca y esté oculto el tile, se le asigna una mark
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        #Cambiamos el aliniamiento de nuestra marca
        marca=f"{tiles[mark]:>2}"
        #Se escribe en el tile
        write(marca,font=('Arial', 30, 'normal'))
    #Se actualiza
    update()
    ontimer(draw, 100)
    
#Se llaman a las funciones (también de librerías)
shuffle(tiles) 
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
