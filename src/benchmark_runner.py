"""
OpenFraudLabs Benchmark Runner.
"""

from src.metrics import evaluate_model
from src.train import train_models


def benchmark_models(
    X_train,
    X_test,
    y_train,
    y_test,
):
    """
    Train and evaluate all models.
    """

    results = []

    trained_models = train_models(
        X_train,
        y_train,
    )

    for name, model in trained_models.items():

        print(
            f"Evaluating {name}..."
        )

        y_pred = model.predict(
            X_test,
        )

        y_prob = model.predict_proba(
            X_test,
        )[:, 1]

        metrics = evaluate_model(
            y_test,
            y_pred,
            y_prob,
        )

        results.append(
            {
                "model": name,
                "recall": metrics["recall"],
                "roc_auc": metrics["roc_auc"],
            }
        )

    return results