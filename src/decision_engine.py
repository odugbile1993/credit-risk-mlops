"""
Decision Engine.

Combines machine learning prediction and
business policy into a final lending decision.
"""

from src.schemas import DecisionReport, PredictionResult, Alert

def generate_decision(
    prediction: PredictionResult,
    alerts: list[Alert],
) -> DecisionReport:
    """
    Generate the final lending decision.
    """

    critical = sum(
        1 for alert in alerts
        if alert.severity == "critical"
    )

    warning = sum(
        1 for alert in alerts
        if alert.severity == "warning"
    )

    if critical > 0:
        recommendation = "Reject"
        approved = False

    elif prediction.risk_band == "High Risk":
        recommendation = "Manual Review"
        approved = False

    elif warning >= 3:
        recommendation = "Manual Review"
        approved = False

    else:
        recommendation = "Approve"
        approved = True

    return DecisionReport(
        prediction=prediction,
        alerts=alerts,
        recommendation=recommendation,
        approved=approved,
    )