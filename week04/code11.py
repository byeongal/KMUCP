score = float(input("백분위(0~100)점수를 입력해 주세요 >>"))

if score >= 30:
    print("당신의 학점은 A입니다.")
elif score >= 70:
    print("당신의 학점은 B입니다.")
else:
    print("당신의 학점은 C입니다.")