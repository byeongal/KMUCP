def average(number_list):
    total = 0
    for each in number_list:
        total = total + each
    return total / len(number_list)

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("평균 :", average(number_list))