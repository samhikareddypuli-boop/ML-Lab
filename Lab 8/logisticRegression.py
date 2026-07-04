# Logistic Regression

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
X = [
    [20], [25], [30], [35], [40],
    [45], [50], [55], [60], [65]
]

# Target (0 = No, 1 = Yes)
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict for a new value
new_data = [[42]]
prediction = model.predict(new_data)

print("Prediction for Age 42:", prediction[0])