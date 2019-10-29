import turtle

t = turtle.Turtle()
t.shape('turtle')
sc = turtle.Screen()
sc.title('배경색칠하기')
sc.bgcolor('black')
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()
sc.mainloop()