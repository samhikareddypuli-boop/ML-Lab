import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [200, 300, 250, 400]
plt.bar(months, sales)
plt.title("Column Graph")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()