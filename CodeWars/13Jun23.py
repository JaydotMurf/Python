# Find The Parity Outlier


def find_outlier(integers):
    evens = [x for x in integers if x % 2 == 0]
    odds = [x for x in integers if x % 2 != 0]

    return odds[0] if len(evens) > 1 else evens[0]


# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
# print(find_outlier([0, 1, 2]))


# The highest profit wins!


def min_max(lst):
    lst.sort()
    return [lst[0], lst[-1]]


def min_max(lst):
    return [min(lst), max(lst)]


# print(min_max([1, 2, 3, 4, 5]))
# print(min_max([2334454, 5]))
# print(min_max([1]))

# Ones and Zeros


def binary_array_to_number(arr):
    return int("".join(str(num) for num in arr), 2)


print(binary_array_to_number([1, 0, 1, 1]))
