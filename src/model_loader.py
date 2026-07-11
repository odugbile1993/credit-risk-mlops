"""
Model loading utilities.

This module is responsible for locating and loading
the trained machine learning model.
"""

import joblib

from src.config import MODEL_PATH


def load_model():
    """
    Load the trained machine learning model.

    Returns
    -------
    object
        Loaded machine learning model.
    """

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    model = joblib.load(MODEL_PATH)

    return model