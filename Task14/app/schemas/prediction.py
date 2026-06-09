from pydantic import BaseModel

class PredictionRequest(BaseModel):
    experience: int
    education_level: int
    certifications: int