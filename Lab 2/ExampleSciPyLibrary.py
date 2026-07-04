from scipy import stats
data = [10, 20, 30, 40, 50]
print("Mean:", stats.tmean(data))
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))