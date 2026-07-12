"""
Explainability service.

Generates SHAP explanations
for borrower predictions.
"""

import shap

from src.feature_mapper import get_feature_info
from src.model_loader import load_model
from src.schemas import Explanation


class ExplainerService:
    """
    Generates SHAP explanations using SHAP.
    """

    def __init__(self):
        """
        Initialize the SHAP explainer.
        """
        self.model = load_model()
        self.explainer = shap.TreeExplainer(self.model)

    def explain(self, input_df):
        """
        Generate SHAP explanation.

        Parameters
        ----------
        input_df : pandas.DataFrame

        Returns
        -------
        shap.Explanation
        """
        return self.explainer(input_df)

    def top_features(self, input_df, top_n=3):
        """
        Return the most influential features
        as Explanation objects.

        Parameters
        ----------
        input_df : pandas.DataFrame
        top_n : int, optional
            Number of top features to return.

        Returns
        -------
        list[Explanation]
        """

        explanation = self.explain(input_df)

        values = explanation.values[0]
        feature_names = explanation.feature_names

        ranked = sorted(
            zip(feature_names, values),
            key=lambda x: abs(x[1]),
            reverse=True,
        )

        explanations = []

        for feature, value in ranked[:top_n]:

            direction = (
                "Increase Risk"
                if value > 0
                else "Reduce Risk"
            )

            info = get_feature_info(feature)

            explanations.append(
                Explanation(
                    feature=info["name"],
                    contribution=float(value),
                    direction=direction,
                    description=(
                        info["increase"]
                        if value > 0
                        else info["decrease"]
                    ),
                )
            )

        return explanations