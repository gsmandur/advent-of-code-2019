import sys


def in_order_digits(num: int):
    # make sure digits are in descending order
    prev_digit = 9
    while (num > 0):
        digit = num % 10
        if digit > prev_digit:
            return False

        num = num // 10
        prev_digit = digit
    return True


def exist_adjacent_digits(num: int):
    # make sure there are 2 digits that are the same
    prev_digit = -1
    while (num > 0):
        digit = num % 10
        if digit == prev_digit:
            return True

        num = num // 10
        prev_digit = digit
    return False


# puzzle input
start = 134564
end = 585159

valid_count = 0
for num in range(start, end+1):
    if in_order_digits(num) and exist_adjacent_digits(num):
        valid_count += 1
print(valid_count)
