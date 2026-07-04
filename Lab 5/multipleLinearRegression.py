import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Area": [1000, 1200, 1500, 1800, 2000],
    "Bedrooms": [2, 2, 3, 3, 4],
    "Price": [300000, 350000, 450000, 500000, 600000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (Independent variables)
X = df[["Area", "Bedrooms"]]

# Target (Dependent variable)
y = df["Price"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict house price
predicted_price = model.predict([[1600, 3]])

print("Predicted House Price =", predicted_price[0])