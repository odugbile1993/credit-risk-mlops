"""
Evaluation Service.

Runs the complete borrower evaluation pipeline.
"""

from src.business_rules import check_credit_policy
from src.decision_engine import generate_decision
from src.explainability.explainer import ExplainerService
from src.predictor import predict
from src.preprocessing import prepare_input


class EvaluationService:
    """
    Coordinates the complete
    borrower evaluation workflow.
    """

    def __init__(self):
        self.explainer = ExplainerService()

    def evaluate(self, borrower):
        """
        Evaluate a borrower from
        start to finish.
        """

        # Prepare model input
        input_df = prepare_input(borrower)

        # Machine Learning prediction
        prediction = predict(input_df)

        # Business policy
        alerts = check_credit_policy(borrower)

        # Explainability
        explanations = self.explainer.top_features(input_df)

        # Final decision
        report = generate_decision(
            prediction=prediction,
            alerts=alerts,
            explanations=explanations,
        )

        return report