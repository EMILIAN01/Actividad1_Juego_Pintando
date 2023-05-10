"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


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


def circle(start, end):
    """Draw circle from start to end."""
    radius = distance(start, end)
    up()
    goto(start.x, start.y - radius)
    down()
    begin_fill()
    circle(radius)
    end_fill()
    
def rectangle(start, end):
    # Ir al primer punto
    up()
    goto(start.x, start.y)
    down()

    # Dibujar el rectángulo
    begin_fill()
    for _ in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    end_fill()



def triangle(start, end):
    import math

def triangle(start, end):
    """Draw equilateral triangle from start to end."""
    length = (end - start).mag()
    height = math.sqrt(3) / 2 * length
    midpoint = (start + end) / 2
    angle = math.atan2(end.y - start.y, end.x - start.x)
    up()
    goto(midpoint.x, midpoint.y - height / 2)
    setheading(math.degrees(angle) + 60)
    down()
    for _ in range(3):
        forward(length)
        left(120)
    up()



def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
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
onkey(lambda: color('pink'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
