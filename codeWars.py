"""
# Sum of two lowest positive integers

def sum_two_smallest_numbers(numbers):
    # return sorted(numbers)[0] + sorted(numbers)[1]
    return sum(sorted(numbers)[:2])


my_numbers = [19, 5, 42, 2, 77]
print(sum_two_smallest_numbers(my_numbers))
"""
