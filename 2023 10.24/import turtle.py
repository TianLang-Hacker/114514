import turtle

# 创建Turtle画布
screen = turtle.Screen()
screen.bgcolor("white")

# 创建Turtle对象
pen = turtle.Turtle()
pen.speed(0)  # 设置绘制速度，0为最快

# 定义正方形的边长和点的大小
side_length = 200
dot_size = 10

# 计算每行应绘制的点数
dots_per_side = 100 // 4

# 绘制实心正方形
for _ in range(4):
    for _ in range(dots_per_side):
        pen.dot(dot_size)
        pen.penup()
        pen.forward(dot_size)
        pen.pendown()
    pen.penup()
    pen.setx(0)
    pen.sety(pen.ycor() + dot_size)
    pen.pendown()

# 隐藏Turtle画笔
pen.hideturtle()

# 关闭Turtle画布
turtle.done()
