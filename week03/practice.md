# 3주차 실습 문제
3주차 실습 문제는 네 자연수 A, B, C, D를 사용자에게 입력 받아, A와 B를 붙인 수와 C와 D를 붙인 수의 합을 구하는 프로그램을 만드는 것 이다.
두 수를 붙이기 위해서는 문자열 합치기 연산을 해야하고, 그 이후 합친 문자열을 숫자로 변경한 다음 정수의 합 연산을 해야한다.
문자열을 합치는 연산은 `+` 이고, 문자열을 정수로 변경하는 함수는 `int`이고, 정수의 합 연산은 `+`이다.
```python
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(int(a+b) + int(c+d))
```

* 출처 : https://www.acmicpc.net/problem/10824
