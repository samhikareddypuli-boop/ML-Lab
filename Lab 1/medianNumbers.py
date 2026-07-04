numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median = numbers[n // 2]
print("Median =", median)