def calculate_stats(str):
    numbers = [str]
    print("Sum of numbers: ", sum(numbers))
    if sum(numbers) > 100:
        print("Большая сумма")
    print("Max number: ", max(numbers))
    print("Min number: ", min(numbers))
