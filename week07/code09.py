import turtle
t = turtle.Turtle()
color_list = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
for i in range(7):
    radius = (i + 1) * 10
    t.color(color_list[i])
    t.circle(radius)
turtle.mainloop()