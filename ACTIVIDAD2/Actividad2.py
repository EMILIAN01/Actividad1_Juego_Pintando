from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#definicon de colores
colors = ['blue', 'orange', 'purple', 'green', 'yellow']
snake_color = colors[randrange(0, len(colors))] # Escoge un color al azar de la lista
food_color = colors[randrange(0, len(colors))] # Escoge otro color al azar de la lista
while food_color == snake_color:
    # Asegurarse de que la comida no tenga el mismo color que la serpiente
    food_color = colors[randrange(0, len(colors))]

def choose_color(colors, current_color):
    """Choose a color different from the current one."""
    new_color = current_color
    while new_color == current_color:
        new_color = colors[randrange(0, len(colors))]
    return new_color

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

#comida 
def move_food():
    """Move food one step at a time."""
    newfood = food.copy()
    moves = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = moves[randrange(0, len(moves))]

    newfood.move(move)
    if inside(newfood):
        food.move(move)
    ontimer(move_food,200)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

        # Hacer que la serpiente crezca
        snake.append(snake[-1].copy())

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move_food()
move()
done()