"""
OpenFraudLabs Model Registry.
"""

from catboost import CatBoostClassifier
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.linear_model import LogisticRegression


def get_models():
    """
    Return candidate models.
    """

    return {
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            random_state=42,
        ),
        "Random Forest": RandomForestClassifier(
            random_state=42,
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            random_state=42,
        ),
        "CatBoost": CatBoostClassifier(
            random_state=42,
            verbose=False,
        ),
    }