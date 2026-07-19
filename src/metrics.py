"""
OpenFraudLabs Metrics Toolkit.

Provides utilities for evaluating
machine learning model performance.
"""

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


def evaluate_model(
    y_true,
    y_pred,
    y_prob,
):
    """
    Evaluate a classification model.
    """

    return {
        "accuracy": accuracy_score(
            y_true,
            y_pred,
        ),
        "precision": precision_score(
            y_true,
            y_pred,
        ),
        "recall": recall_score(
            y_true,
            y_pred,
        ),
        "f1_score": f1_score(
            y_true,
            y_pred,
        ),
        "roc_auc": roc_auc_score(
            y_true,
            y_prob,
        ),
    }


def print_evaluation_report(
    metrics: dict,
):
    """
    Display an OpenFraudLabs
    evaluation report.
    """

    print()
    print("=" * 60)
    print("        OPENFRAUDLABS MODEL EVALUATION REPORT")
    print("=" * 60)

    print()

    print(
        f"Accuracy              : {metrics['accuracy']:.2%}"
    )

    print(
        f"Precision             : {metrics['precision']:.2%}"
    )

    print(
        f"Recall                : {metrics['recall']:.2%}"
    )

    print(
        f"F1 Score              : {metrics['f1_score']:.2%}"
    )

    print(
        f"ROC-AUC               : {metrics['roc_auc']:.2%}"
    )

    print()

    print("Business Interpretation")
    print("-" * 60)

    if metrics["recall"] < 0.30:

        print(
            "• Model misses a significant number of "
            "high-risk borrowers."
        )

    elif metrics["recall"] < 0.60:

        print(
            "• Model demonstrates moderate ability "
            "to identify defaults."
        )

    else:

        print(
            "• Model demonstrates strong ability "
            "to identify defaults."
        )

    if metrics["roc_auc"] >= 0.85:

        print(
            "• Model exhibits excellent discriminatory power."
        )

    print()

    print("=" * 60)