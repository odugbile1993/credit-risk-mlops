"""
Decision Engine.

Combines machine learning prediction,
business policy, and explainability into
a final lending decision.
"""

from src.schemas import (
    Alert,
    DecisionReport,
    Explanation,
    PredictionResult,
)


def generate_decision(
    prediction: PredictionResult,
    alerts: list[Alert],
    explanations: list[Explanation],
) -> DecisionReport:
    """
    Generate the final lending decision.

    Parameters
    ----------
    prediction : PredictionResult
    alerts : list[Alert]
    explanations : list[Explanation]

    Returns
    -------
    DecisionReport
    """

    critical = sum(
        1
        for alert in alerts
        if alert.severity == "critical"
    )

    warning = sum(
        1
        for alert in alerts
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
        explanations=explanations,
        recommendation=recommendation,
        approved=approved,
    )