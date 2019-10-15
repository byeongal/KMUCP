import turtle
text = turtle.textinput("문자열", "문자열을 입력해 주세요.")
t = turtle.Turtle()
t.write(text, move=True)
turtle.mainloop()