from src.schemas import Borrower
from src.preprocessing import prepare_input
from src.explainability.explainer import ExplainerService


borrower = Borrower(
    revolving_utilization=0.5,
    age=35,
    past_due_30_59=0,
    debt_ratio=0.4,
    monthly_income=5000,
    open_credit_lines=5,
    times_90_days_late=0,
    real_estate_loans=1,
    past_due_60_89=0,
    dependents=2,
)

input_df = prepare_input(borrower)

service = ExplainerService()

print("\nTop SHAP Explanations\n")

for explanation in service.top_features(input_df):

    print(f"Feature      : {explanation.feature}")
    print(f"Contribution : {explanation.contribution:.4f}")
    print(f"Direction    : {explanation.direction}")
    print(f"Description  : {explanation.description}")
    print("-" * 60)