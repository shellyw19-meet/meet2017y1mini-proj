import turtle
import random

turtle.tracer(1,0)

size_x=800
size_y=500
turtle.setup(size_x , size_y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[1]

    x_pos += SQUARE_SIZE

    my_pos = (x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    s = snake.stamp()
    stamp_list.append(s)

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

direction = UP

def up():
    global direction
    direction = UP
    move_snake()
    print("You pressed the up key!")

def down():
    global direction
    direction = DOWN
    move_snake()
    print("You pressed the down key!")

def left():

def right():
    global direction
    direction = RIGHT
    move_snake()
    print("You pressed the right key!")

turtle.onpresskey(up, UP_ARROW)
turtle.onpresskey(down, DOWN_ARROW)
turtle.onpresskey(left, LEFT_ARROW)
turtle.onpresskey(right, RIGHT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my pos[1]

    if direction === RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction == LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left")
    elif direction == down:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif direction == UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")

    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)

    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pop_list.pop(0)































    




















    
























    
    
