from sklearn.datasets import (
    make_classification,
)
from sklearn.model_selection import (
    train_test_split,
)

from src.benchmark import (
    print_benchmark_report,
)
from src.benchmark_runner import (
    benchmark_models,
)

X, y = make_classification(
    n_samples=5000,
    n_features=10,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

results = benchmark_models(
    X_train,
    X_test,
    y_train,
    y_test,
)

print_benchmark_report(
    results,
)