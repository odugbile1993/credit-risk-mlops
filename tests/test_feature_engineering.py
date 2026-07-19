from src.feature_engineering import (
    age_band,
    delinquency_score,
    disposable_income,
    estimated_monthly_debt,
    income_per_dependent,
    utilization_band,
)

print("\n=== FEATURE ENGINEERING TESTS ===\n")

print(
    "Income Per Dependent:",
    income_per_dependent(
        monthly_income=5000,
        dependents=2,
    ),
)

print(
    "Estimated Monthly Debt:",
    estimated_monthly_debt(
        debt_ratio=0.4,
        monthly_income=5000,
    ),
)

print(
    "Disposable Income:",
    disposable_income(
        monthly_income=5000,
        debt_ratio=0.4,
    ),
)

print(
    "Delinquency Score:",
    delinquency_score(
        past_due_30_59=1,
        past_due_60_89=2,
        times_90_days_late=1,
    ),
)

print(
    "Utilization Band:",
    utilization_band(0.8),
)

print(
    "Age Band:",
    age_band(35),
)