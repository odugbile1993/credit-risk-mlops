from src.metrics import (
    evaluate_model,
    print_evaluation_report,
)

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]
y_prob = [0.10, 0.85, 0.40, 0.20, 0.90]

metrics = evaluate_model(
    y_true,
    y_pred,
    y_prob,
)

print_evaluation_report(
    metrics,
)