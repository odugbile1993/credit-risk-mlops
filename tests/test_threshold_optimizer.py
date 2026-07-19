import pandas as pd

from sklearn.model_selection import train_test_split

from src.model_registry import get_models
from src.threshold_optimizer import (
    optimize_threshold,
)

df = pd.read_csv(
    "data/raw/project_train_data.csv"
)

df = df.drop(
    columns=["Id"]
)

df = df.fillna(
    df.median(numeric_only=True)
)

X = df.drop(
    columns=["SeriousDlqin2yrs"]
)

y = df["SeriousDlqin2yrs"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = get_models()[
    "Gradient Boosting"
]

model.fit(
    X_train,
    y_train,
)

y_prob = model.predict_proba(
    X_test,
)[:, 1]

results = optimize_threshold(
    y_test,
    y_prob,
)

print()
print("=" * 70)
print("OPENFRAUDLABS THRESHOLD OPTIMIZATION REPORT")
print("=" * 70)
print()

print(
    f"{'Threshold':<15}"
    f"{'Precision':<15}"
    f"{'Recall':<15}"
)

print("-" * 70)

for result in results:

    print(
        f"{result['threshold']:<15}"
        f"{result['precision']:.2%}{'':<8}"
        f"{result['recall']:.2%}"
    )