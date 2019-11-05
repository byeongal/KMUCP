def range_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total = total + i
    return total

print("1부터 100까지의 합은", range_sum(1, 100))