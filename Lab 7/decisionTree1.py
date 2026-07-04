# Decision Tree with Parameter Tuning

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
X = [[22, 0], [25, 1], [47, 1], [52, 0], [46, 1], [56, 0], [48, 1], [33, 0]]

# Target (0 = No, 1 = Yes)
y = [0, 0, 1, 1, 1, 1, 1, 0]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create Decision Tree with parameter tuning
model = DecisionTreeClassifier(max_depth=3)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))