"""
OpenFraudLabs Threshold Optimizer.
"""

from sklearn.metrics import (
    precision_score,
    recall_score,
)


def evaluate_threshold(
    y_true,
    y_prob,
    threshold,
):
    """
    Evaluate model performance at a
    given probability threshold.
    """

    y_pred = (
        y_prob >= threshold
    ).astype(int)

    return {
        "threshold": threshold,
        "precision": precision_score(
            y_true,
            y_pred,
            zero_division=0,
        ),
        "recall": recall_score(
            y_true,
            y_pred,
        ),
    }


def optimize_threshold(
    y_true,
    y_prob,
):
    """
    Evaluate multiple thresholds.
    """

    thresholds = [
        0.10,
        0.15,
        0.20,
        0.25,
        0.30,
        0.35,
        0.40,
        0.50,
    ]

    results = []

    for threshold in thresholds:

        results.append(
            evaluate_threshold(
                y_true,
                y_prob,
                threshold,
            )
        )

    return results