import turtle

screen= 600
grid = 30
half = int(screen/2)

def jjbar(startlong, startlat, increment,gap, height, width, color):

    #make rectangle
    turtle.penup()
    turtle.goto(startlong + (increment+(gap*increment))*grid,startlat)
    turtle.setheading(90)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range (0,2):
        turtle.forward(int(height)*grid)
        turtle.right(90)
        turtle.forward(width*grid)
        turtle.right(90)
    turtle.end_fill()
    turtle.pensize(1)
    turtle.pencolor("white")


turtle.speed(0)
turtle.setup(screen+150,screen+150)
turtle.screensize(screen+100, screen+100,"black")
turtle.pencolor("white")
turtle.penup()
turtle.goto( half,-half)
turtle.pendown()
turtle.pensize(3)
turtle.goto(-half,-half)
turtle.goto(-half,half)
turtle.pensize(1)
turtle.penup()
turtle.goto(-half,0)
turtle.left(90)
i=1
n=int(screen/grid)
for i in range(n):
    turtle.penup()
    turtle.goto(-half,-half+(grid*i))
    turtle.pendown()
    turtle.goto(half-grid,-half+(grid*i))
    turtle.penup()
    turtle.goto(-half+grid*i,-half)
    turtle.pendown()
    turtle.goto(-half+grid*i,half-grid)
    i = i+1


data = [1,4,7,5,2,7,8,4,1,3]
for i in range(len(data)):
    jjbar(-half, -half, i,1, data[i],1,"red")

turtle.exitonclick()
