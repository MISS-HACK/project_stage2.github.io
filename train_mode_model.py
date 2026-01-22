from sklearn.tree import DecisionTreeClassifier
import joblib

# Inputs: [SOC_EMG, SOC_EV1, SOC_EV2]
X = [
    [20, 70, 70],   # EMG low → priority
    [30, 60, 65],
    [50, 50, 50],   # balanced
    [80, 40, 40],
    [90, 90, 90],   # all high
    [15, 80, 80]    # reverse possibility
]

# Modes
# 1 = Normal
# 2 = Emergency Priority
# 3 = Reverse Charging
y = [2, 2, 1, 1, 1, 3]

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, y)

joblib.dump(model, "mode_model.pkl")
print("Model trained and saved")
