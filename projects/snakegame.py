import turtle #graphics library
import time
import random

#delay time per frame
delay = 0.1

game_started = False
start_time = 0

#for score and time
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)


#set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600) #window of 600 x 600 pixels
wn.tracer(0) #turns off the screen updates

#adding grid to the window
grid = turtle.Turtle()
grid.hideturtle()
grid.speed(0)
grid.penup()
grid.color('gray')
for x in range(-280,300,20):
    for y in range(-280,300,20):
        grid.goto(x, y)
        grid.dot(2)

#Snake head
head = turtle.Turtle() #creating a turtle object and storing it in 'head'
head.speed(2)
head.shape('square') #controls animation speed of the turtle
head.color('green')
head.penup()
head.goto(50,50)
head.direction = 'stop'

#Snake food
food = turtle.Turtle() 
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments = []


#Functions
def go_up():
    global game_started, start_time
    if head.direction != 'down':
        if not game_started:
            start_time = time.time()
            game_started = True
        message.clear()
        head.setheading(90)  
        head.direction = 'up'
def go_down():
    global game_started, start_time
    if head.direction != 'up':
        if not game_started:
            start_time = time.time()
            game_started = True
        message.clear()
        head.setheading(270)  
        head.direction = 'down'
def go_left():
    global game_started, start_time
    if head.direction != 'right':
        if not game_started:
            start_time = time.time()
            game_started = True
        message.clear()
        head.setheading(180)  
        head.direction = 'left'
def go_right():
    global game_started, start_time
    if head.direction != 'left':
        if not game_started:
            start_time = time.time()
            game_started = True
        message.clear()
        head.setheading(0)  
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

def game_over():
    message.goto(0,0)
    message.write("GAME OVER", align="center", font=("Arial",24,"bold"))

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

message = turtle.Turtle()
message.hideturtle()
message.color('yellow')
message.penup()
message.goto(0,0)
message.write("Press any Arrow Keys to Start", align = 'center', font = ('Arial',18,'bold'))



#Main game loop
while True:
    wn.update()

    #updating scoreboard each loop
    pen.clear()
    if game_started:
        elapsed = int(time.time() - start_time)
    else:
        elapsed = 0
    pen.write(f"Score: {score}   Time: {elapsed}s", align="center", font=("Arial",14,"bold"))

    #collision with food
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        score += 10

        #to extend the body, added a segment
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('light green')
        new_segment.penup()
        new_segment.goto(head.xcor(), head.ycor())
        segments.append(new_segment)
    
    #now moving from last segment
    for index in range(len(segments)-1,0,-1): #0 is excluded
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    
    #when moves out of window, bringing body from opp side
    if head.xcor() > 299:
        head.setx(-299)
    elif head.xcor() < -299:
        head.setx(299)

    if head.ycor() > 299:
        head.sety(-299)
    elif head.ycor() < -299:
        head.sety(299)
    
    #checking collision with body
    for segment in segments[1:]:
        if segment.distance(head) < 10:
            game_over()
            time.sleep(2)
            wn.bye()

    move()
    time.sleep(delay)

wn.mainloop() #keeps the window open and running