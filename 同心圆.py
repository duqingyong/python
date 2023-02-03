# Mame:杜俊
# 性  别：男
# 年  龄：24
# 开发时间：2022/9/7 20:16
import turtle as t

t.setup(800, 800)  # 画布尺寸
t.pensize(2)  # 画笔粗细
for i in range(20):
    t.speed(0)
    if i % 2 == 0:
        t.pencolor('red')
    else:
        t.pencolor('blue')
    t.circle(180)  # 半径
    # t.fd(20)  #forward()
    t.forward(20)
    t.left(31)  # 往左转31度
    t.hideturtle()
    t.showturtle()
t.done()
