# 5주차 실습 문제
터틀 그래픽을 이용하여 사용자에게 `n`을 입력 받아 정 `n`각형을 그리고, 해당 `n`각형을 `green`으로 색칠하는 프로그램을 작성 하세요. 단 `n`은 3이상의 자연수 이며, 도형의 크기는 자유롭게 설정 합니다.


#### 제한 사항
* `circle`함수를 사용하여 정 `n`각형을 그린 경우 최대 점수의 `80%`만 받을 수 있습니다.

#### 참고코드
```python
import turtle

n = int(turtle.numinput("숫자", "3이상의 자연수 :", minval=3))
t = turtle.Turtle()
'''
CODE
'''
turtle.mainloop()
```