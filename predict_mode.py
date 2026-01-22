import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath('C:\Users\Telan\Desktop\toolbox\matlab\appcontainer\web\release\dashboard'))
model_path = os.path.join(BASE_DIR, "mode_model.pkl")

model = joblib.load(model_path)

def predict_mode(soc_em, soc_ev1, soc_ev2):
    X = [[soc_em, soc_ev1, soc_ev2]]
    return int(model.predict(X)[0])

