def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("자연수를 입력 해주세요. :"))
if is_even(number):
    print("짝수입니다.")
else:
    print("홀수입니다.")