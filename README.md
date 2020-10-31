# Figuritas-Oliart
Paint: 
Este programa le permite al usuario dibujar líneas y figuras en distintos colores.
Al programa se le agregó un nuevo color, el amarillo. Además se desarrollaron las siguientes funciones para dibujar las figuras

-Función “circle”: esta función se encarga de dibujar un círculo cuando el usuario lo solicita. El usuario da dos puntos: el centro y cualquier punto de la circunferencia.

-Función “rectangle”: esta función dibuja un rectángulo. El usuario da dos puntos que indican dos esquinas del rectángulo.

-Función “triangle”: esta función tenía el objetivo de dibujar un triángulo, de acuerdo a los puntos iniciales y finales brindados por el usuario. Lo primero que se realizaba, era alzar el pincel para dejar dibujar, posteriormente, lo colocamos en la posición que estableció el jugador con su cursor; una vez ahí, movemos el pincel al segundo punto dado (se dibuja  la hipotenusa), después el pincel se mueve verticalmente a la coordenada Y del primer punto y finalmente se regresa a las coordenadas del primer punto. Por último, rellenamos el área para conformar el triángulo.


Pacman:
Una versión simplificada del juego clásico de arcade “Pacman” la cual corre a base de python3 y las librerías de turtle y myfreegames que le permite al usuario jugar en una modalidad clásica recogiendo puntos blancos para aumentar su score mientras que debe de huir de 3 fantasmas.

-Función Square: dibuja un cuadrado utilizando el path del punto x y y.

-Función offset: regresa el desplazamiento del punto para el tablero.

-Función valid: revisa si el punto que recibe como parámetro es un punto válido dentro del tablero de juego.

-Función world: dibuja el tablero, modificando el color del fondo y del path.

-Función move: controla el movimiento del pacman a base de inputs y el de los fantasmas a base de randoms y variables fijas, revisa por colisión con objetos que den puntos y también por colisiones con fantasmas, manejando los distintos estados del juego.

-Función change:
Cambia la dirección del jugador en caso de que este de un input válido.


Snakes: 
Snakes es un videojuego que consiste en el consumo de puntos (comida) distribuidos alrededor del mapa, con la finalidad de incrementar la longitud de tu personaje (En este caso, una serpiente). El juego finaliza cuando la serpiente colisiona consigo misma (Ya que esta puede moverse en las 4 direcciones disponibles en un canvas 2D). 

Los parámetros iniciales involucran establecer la posición vectorial de la serpiente, su alimento, y la dirección a la que se desplaza, aunado a la serie de colores que se les colocaron a los elementos (Los cuales se determinan al azar a través de un número aleatorio entre 0 y 4, para así poder establecer 4 colores) 

-Función “change”: nos permite modificar la posición a la que apunta la dirección de la cabeza de acuerdo a los nuevos valores que provea el usuario. 

-Función “change_food”: caso análogo a la función “change” pero aplicado a la posición de la comida. 

-Función “move”: se encarga de desplazar cada uno de los recuadros que conforman la serpiente. Lo primero que se realiza es generar una copia del último elemento (su cabeza) para posteriormente aplicarle la función move con dirección a lo que posee la variable “aim”. Una vez realizado eso, evaluamos que la serpiente no haya colapsado consigo misma o con los límites del canvas (En caso de que sí, se colocará un cuadro rojo en la cabeza, y el juego finalizará) 
 
Una vez que la cabeza se ve desplazada, la añadimos de nueva cuenta a nuestra serpiente y evaluamos si esta se encuentra en la misma posición que el objeto “comida” (En caso de que sí, este desaparecerá, se colocará en un lugar al azar del canvas y se aumentará en uno el tamaño de la serpiente). 


Juego de Memoria:
Memory es un videojuego de memoria que consiste en un tablero cuadriculado en blanco cuyos elementos tienen un identificador; cada elemento tiene una pareja con el mismo identificador. Al momento de darle click a un elemento del tablero, este mostrará su número de identificador, el tablero sólo puede mostrar dos identificadores a la vez, y si ambos identificadores de los elementos son los mismos, entonces se despliega su contenido, en este caso el contenido es un pedazo de una imagen de un carro.

-Función square: es la función que básicamente crea nuestro tablero en blanco con cuadrículas de líneas negras.

-Función index: convierte los índices de cada cuadrito del tablero en coordenadas x, y.

-Función printTaps: función que imprime el número de “taps” (movimientos) que ha realizado el usuario.

-Función terminado: función que imprime en pantalla un mensaje de que el juego se ha completado (en caso de que todos los cuadritos estén descubiertos).

-Función tap: determina si el “tap” que da el usuario es igual al anterior “tap” que dió, en caso de que tenga el mismo identificador se revela esa parte de la imagen del carro. (Esta función también llama a printTaps y terminado).


-Función draw: dibuja las partes de la imagen de cada cuadrito y sus identificadores (números enteros). En esta función se modificó el write de los identificadores de cada tile para que estuvieran centrados en el cuadrito. Además, esta función actualiza constantemente el canvas.
