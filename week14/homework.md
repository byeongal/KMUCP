# 과제 4번
1. 제출 기한은 `12일 04일 00시 00분`부터 `12월 14일 23시 59분`까지이며, 추가 제출은 없습니다.
2. 과제에서 부정 행위(과제 공유, 인터넷을 통한 다운로드)가 발견될 시 *0점 처리* 될 수 있습니다.

## 문제 ( 5점 )
다음 기능을 수행하는 계산기 프로그램을 작성하세요.
1. `clear` 버튼을 누르면 디스플레이 모든 결과를 삭제 하게 하세요. ( 1점 )
2. `=` 버튼을 누르면 디스플레이에 있는 수식의 계산식이 계산 되게 하세요 ( 1점 )
3. `0` 부터 `9`까지의 숫자와 `.`을 입력할 수 있게 버튼을 만드세요 ( 1점 )
4. 사칙연산(`+`, `-`, `*`, `/`)를 지원하도록 버튼을 만드세요 ( 1점 )

## 점수
* 각 부분 문제별로 1점
* 모든 부분 문제를 맞춘 경우 1점

#### 기반 코드
```python
from tkinter import *

window = Tk()
window.title("계산기")

# =
def calculate():
    try:
        result = eval(Entry.get(display))
        display.delete(0, END)
        if isinstance(result, int) or isinstance(result, float):
            display.insert(0, result)
        else:
            display.insert(0, "계산식이 올바르지 않습니다.")
    except:
        display.insert(0, "계산식이 올바르지 않습니다.")


# 숫자 0 ~ 9
def zero() : display.insert(END, 0)
def one() : display.insert(END, 1)
def two() : display.insert(END, 2)
def three() : display.insert(END, 3)
def four() : display.insert(END, 4)
def five() : display.insert(END, 5)
def six() : display.insert(END, 6)
def seven() : display.insert(END, 7)
def eight() : display.insert(END, 8)
def nine() : display.insert(END, 9)

# 계산기 화면
display = Entry(window, width=26)
display.grid(row = 0, column = 0, columnspan=3)

# 7
button_seven = Button(window, text='7', command = seven, width=6)
button_seven.grid(row=1, column=0, columnspan=1)

# 8
button_eight = Button(window, text='8', command = eight, width=6)
button_eight.grid(row=1, column=1, columnspan=1)

# 9
button_nine = Button(window, text='9', command = nine, width=6)
button_nine.grid(row=1, column=2, columnspan=1)

# 4
button_four = Button(window, text='4', command = four, width=6)
button_four.grid(row=2, column=0, columnspan=1)

# 5
button_five = Button(window, text='5', command = five, width=6)
button_five.grid(row=2, column=1, columnspan=1)

# 6
button_six = Button(window, text='6', command = six, width=6)
button_six.grid(row=2, column=2, columnspan=1)

# 1
button_three = Button(window, text='1', command = three, width=6)
button_three.grid(row=3, column=0, columnspan=1)

# 2
button_two = Button(window, text='2', command = two, width=6)
button_two.grid(row=3, column=1, columnspan=1)

# 3
button_one = Button(window, text='3', command = one, width=6)
button_one.grid(row=3, column=2, columnspan=1)

# 0
button_zero = Button(window, text='0', command = zero, width=6)
button_zero.grid(row=4, column=0, columnspan=1)

# =
button_equal = Button(window, text='=', command = calculate, width=14)
button_equal.grid(row=4, column=1, columnspan=2)

window.resizable(width=False, height=False)
window.mainloop()
```

#### 최종 결과
![실습](homework.png)