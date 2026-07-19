from src.benchmark import (
    print_benchmark_report,
)

results = [
    {
        "model": "Gradient Boosting",
        "recall": 0.1971,
        "roc_auc": 0.8661,
    },
    {
        "model": "Random Forest",
        "recall": 0.3510,
        "roc_auc": 0.8710,
    },
    {
        "model": "XGBoost",
        "recall": 0.5530,
        "roc_auc": 0.8910,
    },
]

print_benchmark_report(
    results,
)