import turtle
import time

t = turtle.Turtle()
t.speed(10)
t.screen.setup(1200, 800)
t.screen.bgcolor("#008000")

def ring(color, radius):
	t.fillcolor(color)
	t.begin_fill()
	t.circle(radius)
	t.end_fill()

# рисуем первое ухо
t.up()
t.setpos(-40, 80)
t.down ()
ring('brown', 20)

# рисуем второе ухо
t.up()
t.setpos(40, 80)
t.down()
ring('brown', 20)

#рисуем лицо
t.up()
t.setpos(0, 35)
t.down()
ring('brown', 40)

# рисуем первый глаз
t.up()
t.setpos(-18, 70)
t.down
ring('black', 10)

# рисуем второй глаз
t.up()
t.setpos(18, 70)
t.down()
ring('black', 10)

# рисуем зрачок
t.up()
t.setpos(-18, 73)
t.down()
ring('red', 4)

# рисуем второй зрачок
t.up()
t.setpos(18, 73)
t.down()
ring('red', 4)

# рисуем нос
t.up()
t.setpos(0, 55)
t.down
ring('black', 7)

# рисуем рот
t.up()
t.setpos(0, 55)
t.down()
time.sleep(10)
t.right(90)
t.circle(10, 180)
t.up()
t.setpos(0, 55)
t.down()
time.sleep(10)
t.left(360)
t.circle(10, -180)

t.hideturtle()
t.screen.exitonclick()
t.screen.mainloop()
