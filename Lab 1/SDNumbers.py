numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
std_deviation = variance ** 0.5
print("Standard Deviation =", std_deviation)