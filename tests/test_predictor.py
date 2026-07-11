from src.preprocessing import prepare_input
from src.predictor import predict

input_df = prepare_input(
    revolving_utilization=0.50,
    age=35,
    past_due_30_59=0,
    debt_ratio=0.40,
    monthly_income=5000,
    open_credit_lines=5,
    times_90_days_late=0,
    real_estate_loans=1,
    past_due_60_89=0,
    dependents=0,
)

prediction, probability = predict(input_df)

print("Prediction:", prediction)
print("Probability:", probability)