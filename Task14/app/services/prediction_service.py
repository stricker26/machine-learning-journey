import pandas as pd
import joblib

model = joblib.load(
    "trained_models/salary_model.pkl"
)

def predict_salary(
    experience,
    education_level,
    certifications
):
    input_data = pd.DataFrame([
        {
            "experience": experience,
            "education_level": education_level,
            "certifications": certifications
        }
    ])

    result = model.predict(input_data)

    return float(result[0])