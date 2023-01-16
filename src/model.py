def sum_digits_math(number: int) -> str:
    result = 0
    while number:
        result, number = result + number % 10, number // 10
    return result
