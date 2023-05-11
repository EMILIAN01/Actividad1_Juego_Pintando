"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
#Importa bibliotecas
from turtle import *

from freegames import vector

#Se define la función line que acepta dos argumentos y
#que dibuja líneas utilizando la biblioteca turtle.
def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Se define la función "square" que acepta dos argumentos y
#que dibuja cuadrados utilizando la biblioteca turtle.
def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Se define la función "circulo" que acepta dos argumentos y
#que dibuja círuclos utilizando la biblioteca turtle.
def circulo(start, end):
    """Draw circle from start to end."""
    #calcula radio tomando la diferencia entre los valores inicial y final de x
    #tomando el valor absoluto de este.
    radius = abs(end - start)
    up()
    #se mueve el cursor a la posición para comenzar a dibujar.
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    #Llama a la función "circle" para dibujar el círculo.
    circle(radius)
    #Cierra la figura
    end_fill()

#Se define la función "rectangle" que acepta dos argumentos y
#que dibuja rectángulos utilizando la biblioteca turtle.
def rectangle(start, end):
    """Draw rectangle from start to end."""
    #Ir al primer punto
    up()
    goto(start.x, start.y)
    down()

    #Dibujar el rectángulo
    begin_fill()
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()

#Se define la función "triangle" que acepta dos argumentos y
#que dibuja triángulos utilizando la biblioteca turtle.
def triangle(start, end):
    """Draw triangle from start to end."""
    # Ir al primer punto
    begin_fill()
    up()
    goto(start.x, start.y)
    down()

    # Ir al segundo punto
    goto(end.x, end.y)

    # Ir al tercer punto
    third = vector(start.x, end.y)
    goto(third.x, third.y)

    # Volver al primer punto para cerrar el triángulo
    goto(start.x, start.y)
    end_fill()

#Se define la función "tap", la cuál se llama cuando
#el usuario hace click 
def tap(x, y):
    """Store starting point or draw shape."""
    #Guarda el punto de inicio
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

#Función que guarda diferentes valores en "state".
def store(key, value):
    """Store value in state at key."""
    state[key] = value

#Funciones que definen las acciones que llaman a otras funciones.
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
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()