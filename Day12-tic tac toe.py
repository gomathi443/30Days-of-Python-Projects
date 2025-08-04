import turtle
ws = turtle.Screen()
t = turtle.Turtle()
t.color("Blue")
t.width(2)
t.speed(2)
for i in range(4):
    t.forward(300)
    t.left(90)
for y in [100, 200]:
    t.penup()
    t.goto(0, y)
    t.pendown()
    t.forward(300)
t.left(90)
for x in [100, 200]:
    t.penup()
    t.goto(x, 0)
    t.pendown()
    t.forward(300)
def draw_symbol(symbol, row, col):
    t.penup()
    x = col * 100 + 50   
    y = 250 - row * 100  
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.write(symbol, align="center", font=("Arial", 40, "bold"))
draw_symbol("X", 0, 0)  
draw_symbol("O", 1, 1)  
draw_symbol("X", 2, 2)  
t.hideturtle()
ws.mainloop()
