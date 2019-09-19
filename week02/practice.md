# 2주차 실습 문제
2주차 실습 문제는 BMI계산기를 만드는 과제였습니다. BMI를 계산하는 수식은 다음과 같습니다.

![bmi](https://latex.codecogs.com/gif.latex?bmi%3D%5Cfrac%7Bweight%7D%7Bheight%5E%7B2%7D%7D)

이 때 키의 단위(m)는 미터가 되어야 하고, 몸무게의 단위는 킬로 그램(kg)이 되어야 합니다.
사람의 키와 몸무게는 일반 적으로 185.2cm, 81.3kg 등 실수형태로 표현 됩니다.
따라서 입력으로 정수형(int)이 아닌 실수형(float)으로 변환을 해야 합니다.

다음으로는 BMI를 계산하는 수식에서 우선 순위를 생각 해야 합니다.
키의 제곱을 먼저 한 다음, 그 값으로 몸무게를 나눠야 합니다.
곱하기와 나누기 사이에는 연산의 우선 순위가 없기 때문에 순서대로 계산을 합니다.
이를 방지 하기 위해서는 분모에 괄호를 넣어 우선 순위를 줘야 합니다.

```python
weight = float(input("몸무게(kg)을 입력해 주세요 >> "))
height = float(input("키(m)를 입력해 주세요 >> "))

bmi = weight / (height * height)

print("당신의 BMI지수는", bmi, "입니다.")
```