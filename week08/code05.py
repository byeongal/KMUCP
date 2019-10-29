balance = float(input("초기 저축액을 입력해 주세요."))
target = float(input("목표 금액을 입력해 주세요."))
interest_rate = float(input("이자율을 입력해 주세요."))
year = 0
while balance < target:
    year = year + 1
    interest = balance * interest_rate
    balance = balance + interest
print(year, "년 뒤에", balance, "만원을 모을 수 있습니다.")