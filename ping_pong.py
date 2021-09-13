#ping-pong game

import turtle
win= turtle.Screen()
win.title("Pong")
win.bgcolor("red")
win.setup(width=800, height=600)
win.tracer(0)



#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B 

# Ball


#Main game Loop
while True:
    win.update() 