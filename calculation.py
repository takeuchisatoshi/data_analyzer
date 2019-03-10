# 合計値
def cal_total(numbers):
    total_number = 0

    for num in numbers:
        total_number += num
    return total_number


# 最大値
def cal_max(numbers):
    max_number = numbers[0]

    for number in numbers:
        if max_number < number:
            max_number = number

    return max_number


# 最小値
def cal_minimum(numbers):
    minimum_number = numbers[0]

    for number in numbers:
        if minimum_number > number:
            minimum_number = number

    return minimum_number


# 平均値
def cal_average(numbers):
    total = 0
    for number in numbers:
        total += number

    size = len(numbers)
    average_number = total / size

    return average_number
