"""
OpenFraudLabs Training Utilities.
"""

from src.model_registry import get_models


def train_models(
    X_train,
    y_train,
):
    """
    Train all candidate models.
    """

    trained_models = {}

    for name, model in get_models().items():

        print(
            f"Training {name}..."
        )

        model.fit(
            X_train,
            y_train,
        )

        trained_models[name] = model

    print()

    print(
        "All models trained successfully."
    )

    return trained_models