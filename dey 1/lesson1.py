from turtle import *


#we want to paint anouse

#staep 1:  drow a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,  200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#first window
penup()
goto(15, 100)
setheading(0)
pendown()

color("yellow")
begin_fill()
for i in range(4) :
    forward(40)
    right(90)
end_fill


#second window
penup()
goto(150, 100)
setheading(0)
pendown()

color("yellow")
begin_fill()
for i in range(4) :
    forward(40)
    right(90)
end_fill


exitonclick()