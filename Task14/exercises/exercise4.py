import pandas as pd
import joblib

model = joblib.load(
    "trained_models/salary_model.pkl"
)

new_data = pd.DataFrame([
    {
        "experience": 5,
        "education_level": 3,
        "certifications": 2
    }
])

salary = model.predict(new_data)

print(salary)