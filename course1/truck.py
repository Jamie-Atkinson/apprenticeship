import turtle

def talloval(r):
    turtle.left(45)
    for loop in range (2):
        turtle.circle(r,90)
        turtle.circle(2/2,90)

turtle.speed("fast")
lat = 480
long = 440
turtle.setup(2*lat+150,2*long+150)
turtle.screensize(2*lat+100,2*long+100, "white")
turtle.pencolor("black")
turtle.penup()
turtle.goto(-340,60)
turtle.pendown()
turtle.goto(260,60)
turtle.goto(450,-40)
turtle.goto(450,-290)
turtle.goto(390,-290)
turtle.left(90)
turtle.circle(60,180)
turtle.right(180)
turtle.goto(-80,-290)
turtle.circle(60,180)
turtle.left(90)
turtle.goto(-340,-290)
turtle.goto(-340,120)
turtle.circle(40,-180)
turtle.left(180)
turtle.circle(40,180)
turtle.left(180)
turtle.circle(40,-180)
turtle.goto(-340,370)
turtle.penup()
turtle.goto(-340,413)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
talloval(30)
turtle.end_fill()
turtle.penup()
turtle.goto(-300,-20)
turtle.write("Happy Glamping!", font=("Comic Sans MS",40,"normal"))
turtle.goto(-300,-25)
turtle.write("just let me die, please, i dont want to go glamping any more, why wont they just let me die, Mr Trump said there would be candy, but there is no candy, only racism, and fake tan. Its awful", font=("Comic Sans MS",4,"normal"))
turtle.goto(0,0)
turtle.exitonclick()
