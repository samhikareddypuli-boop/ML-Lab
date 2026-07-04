numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
print("Variance =", variance)