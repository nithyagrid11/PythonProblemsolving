import turtle #graphics library
import time
import random

delay = 0.1

#set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("lime")
wn.setup(width=600, height=600) #window of 600 x 600 pixels
wn.tracer(0) #turns off the screen updates

#Snake head
head = turtle.Turtle() #creating a turtle object and storing it in 'head'
head.speed(0)
head.shape('square') #controls animation speed of the turtle
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'right'

#Snake food
food = turtle.Turtle() 
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)




#Functions
def go_up():
    head.direction = 'up'
def go_down():
    head.direction = 'down'
def go_left():
    head.direction = 'left'
def go_right():
    head.direction = 'right'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

#Main game loop
while True:
    wn.update()
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

    move()
    time.sleep(delay)

wn.mainloop() #keeps the window open and running