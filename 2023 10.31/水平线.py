import turtle

fd = turtle.Turtle()

turtle.fd = 200
fd_size = 10

fds = 100 // 4


for _ in range(4):
    for _ in range(fds):
        fd.forward(fd_size)
        fd.down()
    fd.setx(0)
    fd.sety(fd.ycor() + fd_size)
    fd.pendown()

fd.hideturtle()

turtle.done()
