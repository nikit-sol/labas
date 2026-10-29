def select_numbers(numbers, threshold):

    result = []
    for x in numbers:
        if 0 <= x <= threshold:
            result.append(x)
    return result
