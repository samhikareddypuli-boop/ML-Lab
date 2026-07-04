numbers = [10, 20, 20, 30, 40, 20, 50]
mode = max(set(numbers), key=numbers.count)
print("Mode =", mode)