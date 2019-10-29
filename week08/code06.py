n = int(input("자연수를 입력해 주세요 : "))
total = 0
while n != 0:
    total = total + n % 10
    n = n // 10
print("각 자리 수의 합은", total, "입니다.")
