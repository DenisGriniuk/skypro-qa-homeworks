import turtle

t = turtle.Turtle()
t.speed(0)
t.screen.setup(1200, 800)

def ring(col, rad):
	t.fillcolor(col)
	t.begin_fill()
	t.circle(rad)
	t.end_fill()

# рисуем первое ухо
t.up()
t.setpos(-40, 80)
t.down
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
t.setpos(-22, 70)
t.down
ring('black', 8)

# рисуем второй глаз
t.up()
t.setpos(22, 70)
t.down()
ring('black', 8)

# рисуем зрачок
t.up()
t.setpos(-22, 73)
t.down()
ring('red', 4)

# рисуем второй зрачок
t.up()
t.setpos(22, 73)
t.down()
ring('red', 4)

# рисуем нос
t.up()
t.setpos(0, 55)
t.down
ring('black', 5)

# рисуем рот
t.up()
t.setpos(0, 55)
t.down()
t.right(90)
t.circle(5, 180)
t.up()
t.setpos(0, 55)
t.down()
t.left(360)
t.circle(5, -180)
t.hideturtle()

t.screen.exitonclick()
t.screen.mainloop()
t.ht()