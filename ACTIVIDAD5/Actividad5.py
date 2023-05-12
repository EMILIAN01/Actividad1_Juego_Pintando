"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""
#Importa librerías
from random import *
from turtle import *
from time import time
from freegames import path

car = path('car.gif') #Carga la imagen del carro
#Se definen variables globales
tiles = ["Estados Unidos","México","Canadá","Brasil","Argentina","Chile","Perú","Colombia","Venezuela","Ecuador","Uruguay","Paraguay","España","Francia","Alemania","Italia",
         "Reino Unido","Irlanda","Suecia","Noruega","Dinamarca","Finlandia","Rusia","China","Japón","Corea del Sur","India","Australia","Nueva Zelanda","Sudáfrica","Nigeria","Egipto"] * 2
state = {'mark': None}
hide = [True] * 64
count=0

#Función que dibuja un cuadrado blanco con contorno negro
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Función que convierte las coordenadas (x, y) 
#en un índice de casilla en la lista "tiles"
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Función que convierte un índice de casilla en las coordenadas (x, y)
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Función que se llama cada vez que el usuario hace clic en una casilla
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global count, tiempoi  # indicamos que estamos usando la variable global 'count'
    count += 1  # aumentamos el contador en 1 en cada llamada
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark']=None

    #Se verifica que si todas las casillas están visibles, 
    if all (not box for box in hide):

        clear()
        up()
        goto(0,0)
        color('black')
        write("GAME OVER. Felicidades!!!", align='center', font=('Arial', 30, 'normal'))        
        input("Presiona Enter para reiniciar...")

#Función que  se encarga de dibujar el tablero 
#y actualizarlo cada vez que se hace una selección
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for i in range(64):
        if hide[i]:
            x, y = xy(i)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 20)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 12, 'normal'))

    # Mostramos el conteo en la pantalla
    up()
    goto(-180, 200)
    color('blue')
    write(f'Taps: {count}', font=('Arial', 16, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 500, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()