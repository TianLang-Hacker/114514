import turtle
#输出一个点
#turtle.dot(100,"#0000FF")

#一行输出114514个点
# for i in range(114514):
#     turtle.dot(i,"#0000FF")
#     turtle.fd(5)

# for i in range(10):
#     turtle.dot(1)
#     turtle.up()
#     turtle.fd(30)
#     turtle.down()


#垂直输出10个点
# turtle.left(90)
# for i in range (10):
#     turtle.dot()
#     turtle.up()
#     turtle.fd(30)
#     turtle.down()

# for j in range (10):
#     turtle.right(90)
# for i in range (10):
#     turtle.dot()
#     turtle.up()
#     turtle.fd(10)
#     turtle.down()

# size = 10  # 正方形的边长

# for i in range(size):
#     for j in range(size):
#         print(".", end=" ")
#     print()

#100个点绘制正方形
# turtle.left(114)
# turtle.color("#00FF00")
# for i in range(10):
#     for i in range(10):
#         turtle.dot()
#         turtle.up()
#         turtle.fd(30)
#         turtle.down()
#     turtle.up()
#     turtle.fd(-300)
#     turtle.right(90)
#     turtle.fd(30)
#     turtle.right(-90)
#     turtle.down()

#画五角星，黄色边框，红色填充

# turtle.left(0)
# turtle.fd(100)
# turtle.left(-144)
# turtle.fd(100)
# turtle.left(-144)
# turtle.fd(100)
# turtle.left(-144)
# turtle.fd(100)
# turtle.left(-144)
# turtle.fd(100)

turtle.colormode(255)
turtle.color((255,255,0),(255,0,0))
turtle.begin_fill()

for i in range(5):
    turtle.fd(300)
    turtle.right(114)

turtle.end_fill()

# input()
