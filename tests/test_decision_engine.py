from src.schemas import Borrower
from src.preprocessing import prepare_input
from src.predictor import predict
from src.business_rules import check_credit_policy
from src.decision_engine import generate_decision


borrower = Borrower(
    revolving_utilization=1.5,
    age=20,
    past_due_30_59=0,
    debt_ratio=6,
    monthly_income=800,
    open_credit_lines=5,
    times_90_days_late=4,
    real_estate_loans=1,
    past_due_60_89=0,
    dependents=3,
)

input_df = prepare_input(borrower)

prediction = predict(input_df)

alerts = check_credit_policy(borrower)

decision = generate_decision(
    prediction,
    alerts,
)

print("\n===== Decision Report =====")

print("Prediction     :", decision.prediction.prediction)

print("Probability    :", round(decision.prediction.probability, 4))

print("Risk Band      :", decision.prediction.risk_band)

print("Recommendation :", decision.recommendation)

print("Approved       :", decision.approved)

print("Alerts         :", len(decision.alerts))