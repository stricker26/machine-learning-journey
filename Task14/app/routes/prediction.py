from fastapi import APIRouter
from app.schemas.prediction import PredictionRequest
from app.services.prediction_service import predict_salary

router = APIRouter()

@router.post("/predict")
def predict(data: PredictionRequest):

    salary = predict_salary(
        data.experience,
        data.education_level,
        data.certifications
    )

    return {
        "predicted_salary": f"{salary:.2f}"
    }