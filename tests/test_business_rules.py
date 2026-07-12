from src.business_rules import check_credit_policy
from src.schemas import Borrower


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

alerts = check_credit_policy(borrower)

print(f"Total Alerts: {len(alerts)}\n")

for i, alert in enumerate(alerts, start=1):
    print(f"Alert {i}")
    print(f"Severity : {alert['severity']}")
    print(f"Title    : {alert['title']}")
    print(f"Reason   : {alert['reason']}")
    print("-" * 50)