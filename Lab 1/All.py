import statistics
data = list(map(float, input('Enter numbers separated by space: ').split()))
mean = statistics.mean(data)
median = statistics.median(data)
try:
    mode = statistics.mode(data)
except statistics.StatisticsError:
    mode = "No unique mode"
variance = statistics.variance(data)
std_dev = statistics.stdev(data)
print('\n----- Statistical Measures -----')
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_dev)