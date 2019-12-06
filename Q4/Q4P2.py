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
    # make sure there are only 2 digits that are the same
    prev_digit = -1
    # num is a 6 digit number
    group_len = 1
    while (num > 0):
        digit = num % 10

        if digit == prev_digit:
            group_len += 1
        elif group_len == 2:
            return True
        else:
            group_len = 1

        num = num // 10
        prev_digit = digit

    return group_len == 2


# puzzle input
start = 134564
end = 585159

valid_count = 0
for num in range(start, end+1):
    if in_order_digits(num) and exist_adjacent_digits(num):
        valid_count += 1
        print(num)
print(valid_count)

# print(exist_adjacent_digits(577789))
