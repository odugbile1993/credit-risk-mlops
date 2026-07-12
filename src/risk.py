"""
Risk classification module.

This module converts prediction probabilities
into business-friendly risk categories.
"""

from src.config import (
    LOW_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
)


def classify_risk(probability: float) -> str:
    """
    Classify borrower risk based on the predicted
    probability of default.

    Parameters
    ----------
    probability : float
        Predicted probability of default.

    Returns
    -------
    str
        Risk category.
    """

    if probability < LOW_RISK_THRESHOLD:
        return "Low Risk"

    elif probability < MEDIUM_RISK_THRESHOLD:
        return "Moderate Risk"

    return "High Risk"