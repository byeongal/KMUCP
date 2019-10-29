n = int(input("자연수를 입력해 주세요 : "))
i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i += 1
print(str(n) + '! 은', factorial)