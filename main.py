# Marcos Gregory Rodrigues Marques - 536281
import turtle
import random

turtle.bgpic('bikini_bottom.gif')

turtle.register_shape('plankton.gif')
turtle.register_shape('crab_burguer.gif')
turtle.register_shape('gary.gif')
turtle.register_shape('spongeheart.gif')

screen = turtle.Screen()
screen.title("Marquinhos's Game - V1.0")
screen.bgcolor('lightgray')

player = turtle.Turtle()
player.shape('gary.gif')
player.up()

# fazer um width e height
arena = turtle.Turtle()
arena.hideturtle()
arena.speed(0)
arena.up()
arena.goto(300, 300)
arena.down()
arena.goto(-300, 300)
arena.goto(-300, -300)
arena.goto(300, -300)
arena.goto(300, 300)

text = turtle.Turtle()
text.speed(0)

heart = turtle.Turtle()
heart.speed(0)
heart.shape('spongeheart.gif')
heart.up()
heart.goto(-280, 320)

heart_two = turtle.Turtle()
heart_two.speed(0)
heart_two.shape('spongeheart.gif')
heart_two.up()
heart_two.goto(-238, 320)

heart_three = turtle.Turtle()
heart_three.speed(0)
heart_three.shape('spongeheart.gif')
heart_three.up()
heart_three.goto(-196, 320)

heart_list = [heart, heart_two, heart_three]

food = turtle.Turtle()
food.up()
food.speed(0)
food.shape('crab_burguer.gif')
food.goto(random.randint(1, 299), random.randint(1, 299))

poison = turtle.Turtle()
poison.speed(0)
poison.up()
poison.shape('plankton.gif')
poison.goto(random.randint(1, 299), random.randint(1, 299))

points = 0
max_points = 0

def write_text(to_sum: int = 0, maximum: int = 0):
    global points
    points += to_sum

    global max_points
    if maximum != 0:
        max_points = maximum

    text.reset()
    text.hideturtle()
    text.up()
    text.goto(30, 300)
    text.write(f'Pontuação: {points} Máximo {max_points}', font=('Courier', 15), align='left', move=True)

write_text()

def is_collided(x, y):
    if x >= 300 or x <= -300:
        return True
    elif y >= 300 or y <= -300:
        return True
    return False

def check_collisions():
    if len(heart_list) != 0:
        if is_collided(poison.xcor() + 10, poison.ycor()):
            poison.back(20)
            poison.setheading(random.randint(0, 360))
        else:
            poison.forward(1)

        if is_collided(food.xcor() + 10, food.ycor()):
            food.back(20)
            food.setheading(random.randint(0, 360))
        else:
            food.forward(1)

        if player.distance(poison.pos()) <= 20:
            heart_list[len(heart_list) - 1].hideturtle()
            heart_list.pop()

            write_text(-points, points)

            player.goto(0, 0)
            poison.goto(random.randint(1, 299), random.randint(1, 299))
        elif player.distance(food.pos()) <= 20:
            write_text(10)

            food.goto(random.randint(1, 299), random.randint(1, 299))
    else:
        screen.bye()

    turtle.ontimer(check_collisions, 0)

def move(ox, oy):
    x, y = player.pos()
    new_x, new_y = x + ox, y + oy

    if not is_collided(new_x, new_y):
        player.goto(new_x, new_y)

def up():
    move(0, 20)

def down():
    move(0, -20)

def right():
    move(20, 0)

def left():
    move(-20, 0)

turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.listen()

check_collisions()

screen.mainloop()
