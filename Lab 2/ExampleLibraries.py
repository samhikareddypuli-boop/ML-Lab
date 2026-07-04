import statistics
import math
import numpy as np
from scipy import stats

data = [10, 20, 30, 40, 50]

print("=== Statistics Library ===")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

print("\n=== Math Library ===")
print("Square Root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of Pi:", math.pi)

arr = np.array(data)
print("\n=== NumPy Library ===")
print("Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("\n=== SciPy Library ===")
print("Mean:", stats.tmean(data))
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))