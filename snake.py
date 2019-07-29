import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQURE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    stamp_id = snake.stamp()
    stamp_list.append(stamp_id)
        
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQURE_SIZE
    snake.goto(x_pos, y_pos)
    new_stamp()


#turtle.mainloop()
