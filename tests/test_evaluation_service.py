from src.evaluation_service import EvaluationService
from src.schemas import Borrower


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

service = EvaluationService()

report = service.evaluate(borrower)

print("\n========== FINAL REPORT ==========\n")

print(f"Prediction      : {report.prediction.prediction}")
print(f"Probability     : {report.prediction.probability:.4f}")
print(f"Risk Band       : {report.prediction.risk_band}")

print(f"\nRecommendation  : {report.recommendation}")
print(f"Approved        : {report.approved}")

print(f"\nPolicy Alerts   : {len(report.alerts)}")

print("\nTop Explanations")

for explanation in report.explanations:
    print(f"- {explanation.feature}")
    print(f"  {explanation.description}")