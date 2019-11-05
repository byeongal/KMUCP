# 9주차 실습 문제
아래의 기반 코드를 이용하여 `start`부터 `end`사이의 모든 윤년(Leap Year)를 출력하는 코드를 작성 하세요.



#### 제한 사항
* `is_leap_year`라는 함수를 반드시 사용할 것

#### 입력 예시
```
1996 2019
```

#### 출력 예시
```
1996
2000
2004
2008
2012
2016
```

#### 기반 코드
```python
# year가 윤년인지 아닌지 판별하는 함수, 윤년인 경우 True를 반환
def is_leap_year(year):
    '''
    코드
    '''

start, end = map(int, input().split())
for year in range(start, end + 1):
    if is_leap_year(year):
        print(year)
```

#### 참고자료
https://ko.wikipedia.org/wiki/%EC%9C%A4%EB%85%84