"""
Prediction service.

This module is responsible for making predictions
using the trained machine learning model.
"""

from src.model_loader import load_model


def predict(input_df):
    """
    Predict credit risk.

    Parameters
    ----------
    input_df : pandas.DataFrame
        Borrower features.

    Returns
    -------
    tuple
        prediction, probability
    """

    model = load_model()

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability