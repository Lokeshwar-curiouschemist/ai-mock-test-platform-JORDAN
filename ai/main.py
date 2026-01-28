import numpy as np

# [speed(sec), accuracy, guess_ratio]
X = np.array([
    [2.0, 0.9, 0.1],  # fast & accurate
    [1.5, 0.4, 0.7],  # guesser
    [6.0, 0.8, 0.1],  # slow but careful
    [2.2, 0.85, 0.2],
    [1.8, 0.5, 0.6],
    [5.5, 0.75, 0.15]
])

# Labels
y = np.array([
    2,  # fast & accurate
    0,  # guesser
    1,  # slow careful
    2,
    0,
    1
])
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
# Prediction

def classify_user(speed, accuracy, guess_ratio):
    features = np.array([[speed, accuracy, guess_ratio]])
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)
    return prediction[0]
