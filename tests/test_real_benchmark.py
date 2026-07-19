import pandas as pd

from sklearn.model_selection import train_test_split

from src.benchmark import (
    print_benchmark_report,
)

from src.benchmark_runner import (
    benchmark_models,
)

df = pd.read_csv(
    "data/raw/project_train_data.csv"
)

# Remove ID column
df = df.drop(
    columns=["Id"]
)

# Handle missing values
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

results = benchmark_models(
    X_train,
    X_test,
    y_train,
    y_test,
)

print_benchmark_report(
    results,
)