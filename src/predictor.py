"""
Prediction service.

This module performs credit risk prediction
using the trained machine learning model.
"""

from src.model_loader import load_model
from src.risk import classify_risk
from src.schemas import PredictionResult


def predict(input_df) -> PredictionResult:
    """
    Predict borrower default risk.

    Parameters
    ----------
    input_df : pandas.DataFrame

    Returns
    -------
    PredictionResult
    """

    model = load_model()

    prediction = int(model.predict(input_df)[0])

    probability = float(model.predict_proba(input_df)[0][1])

    risk_band = classify_risk(probability)

    return PredictionResult(
        prediction=prediction,
        probability=probability,
        risk_band=risk_band,
    )