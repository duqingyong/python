'''让发车转起来'''
import turtle as t
import time


def draw(r):
    '''画一个风车的杆'''
    t.pensize(4)
    t.goto(0, -150)
    t.pensize(1)

    for i in range(4):
        t.setheading(i * 90 + r)
        t.penup()
        t.goto(0, 0)
        t.pendown()

        # 浅蓝色三角形
        t.fillcolor('#50B2F8')
        t.begin_fill()
        t.forward(100)
        t.left(150)
        t.forward(70)
        t.end_fill()

        # 靠近中心的深蓝色三角形
        t.fillcolor('#063EC5')
        t.begin_fill()
        t.left(30)
        t.forward(40)
        t.left(90)
        t.forward(35)
        t.end_fill()


# 用速度1播放一次绘图过程
t.speed(3)
draw(0)

for r in range(0, 360 * 100, 3):
    t.tracer(False)
    t.clear()
    draw(r)
    time.sleep(0.01)
    t.hideturtle()
    t.tracer(True)

t.done()
