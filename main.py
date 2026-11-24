import turtle
import random


screen = turtle.Screen()
screen.title("Abdullah Python Snake Game")
screen.setup(600, 600)
screen.bgcolor("orange")
screen.tracer(0)


snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"


segments = []


food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.color("blue")
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 18, "bold"))



def up():
    if snake.direction != "down":
        snake.direction = "up"

def down():
    if snake.direction != "up":
        snake.direction = "down"

def left():
    if snake.direction != "right":
        snake.direction = "left"

def right():
    if snake.direction != "left":
        snake.direction = "right"



def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)

    elif snake.direction == "down":
        snake.sety(snake.ycor() - 20)

    elif snake.direction == "left":
        snake.setx(snake.xcor() - 20)

    elif snake.direction == "right":
        snake.setx(snake.xcor() + 20)



screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")



def game():

    global score


    for i in range(len(segments) - 1, 0, -1):
        segments[i].goto(segments[i - 1].pos())

    if segments:
        segments[0].goto(snake.pos())

    move()


    if snake.distance(food) < 20:

        food.goto(
            random.randrange(-280, 280, 20),
            random.randrange(-280, 280, 20)
        )

        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("darkgreen")
        new_segment.penup()

        segments.append(new_segment)

        score += 1

        pen.clear()
        pen.write(
            f"Score: {score}",
            align="center",
            font=("Arial", 18, "bold")
        )


    if snake.xcor() > 280 or snake.xcor() < -280:
        game_over()

    if snake.ycor() > 280 or snake.ycor() < -280:
        game_over()


    for segment in segments:
        if segment.distance(snake) < 20:
            game_over()

    screen.update()

    if snake.isvisible():
        screen.ontimer(game, 100)



def game_over():
    snake.hideturtle()

    pen.goto(0, 0)
    pen.write(
        "GAME OVER",
        align="center",
        font=("Arial", 30, "bold")
    )


game()

screen.mainloop()
