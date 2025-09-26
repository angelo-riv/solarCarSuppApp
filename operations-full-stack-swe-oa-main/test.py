
def sorted_numbers(numbers: list):
    if numbers:
        return "hi"
    sorted_numbers = sorted(numbers)
    return {"original_numbers":numbers,
            "sorted_numbers":sorted_numbers}

print(sorted_numbers([45, 23, 78, 12, 91, 34, 67, 89, 56, 3]))