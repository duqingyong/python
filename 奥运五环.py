# Mame:杜俊
# 性  别：男
# 年  龄：24
# 开发时间：2022/9/7 21:46
import turtle as t

t.screensize(400, 500, 'pink')
t.speed(10)
t.pencolor('blue')
t.pensize(9)
t.penup()
t.goto(-210, 0)
t.pendown()
t.circle(100)

t.pencolor('black')
t.penup()
t.goto(10, 0)
t.pendown()
t.circle(100)

t.pencolor('red')
t.penup()
t.goto(230, 0)
t.pendown()
t.circle(100)

t.pencolor('yellow')
t.penup()
t.goto(-110, -125)
t.pendown()
t.circle(100)

t.pencolor('green')
t.penup()
t.goto(120, -125)
t.pendown()
t.circle(100)

t.done()
