def my_sum(seq):
    total = 0
    for each in seq:
        total = total + each
    return total

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_sum(number_list))