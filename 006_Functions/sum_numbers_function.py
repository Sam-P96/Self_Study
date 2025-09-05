def sum_numbers(*value_1: float) -> float:
    result = 0
    for numbers in value_1:
        result += numbers
    return result

print(sum_numbers(3, 4, 5))
nume = (3, 4, 5)

print(sum_numbers(*nume))