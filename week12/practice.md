# 12주차 실습 문제
11월 27일 학생식당 점심 메뉴는 다음과 같습니다.
```
"뚝배기치즈불닭" : 3800,
"쇠고기쌀국수" : 3200,
"참치브라운도시락" : 2900,
"그릴드왕소시지오믈렛라이스" : 4000,
"유산슬덮밥" : 2800
```
아래의 기반 코드를 참고하여 나머지 메뉴를 추가를 하고, 선택된 메뉴의 총 금액을 구하도록 `calculate_price`함수를 완성 하세요.

#### 기반 코드
```python
import tkinter

def calculate_price():
    total_price = 0
    '''
    CODE 02
    '''
    label.configure(text = str(total_price) + "원")


window=tkinter.Tk()
window.title("12주차 실습 :: 점심 메뉴")
window.geometry("400x200")
window.resizable(width=False, height=False)

var_01 = tkinter.IntVar()
button_01 = tkinter.Checkbutton(window, text = "뚝배기치즈불닭", variable = var_01, command = calculate_price)
button_01.pack()
'''
CODE 01
'''

label = tkinter.Label(window, text = "0원")
label.pack()

window.mainloop()
```