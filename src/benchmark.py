"""
OpenFraudLabs Benchmark Toolkit.

Provides utilities for comparing
multiple machine learning models.
"""


def print_benchmark_report(
    results: list[dict],
):
    """
    Print benchmark results.
    """

    print()
    print("=" * 80)
    print(
        "              OPENFRAUDLABS MODEL BENCHMARK REPORT"
    )
    print("=" * 80)

    print()

    print(
        f"{'Model':<25}"
        f"{'Recall':<15}"
        f"{'ROC-AUC':<15}"
    )

    print("-" * 80)

    for result in results:

        print(
            f"{result['model']:<25}"
            f"{result['recall']:.2%}{'':<8}"
            f"{result['roc_auc']:.2%}"
        )

    print()

    champion = max(
        results,
        key=lambda x: x["recall"],
    )

    print("Champion Model")
    print("-" * 80)

    print(
        f"Model      : {champion['model']}"
    )

    print(
        f"Recall     : {champion['recall']:.2%}"
    )

    print(
        f"ROC-AUC    : {champion['roc_auc']:.2%}"
    )

    print()

    print(
        "Recommendation"
    )

    print("-" * 80)

    print(
        f"OpenFraudLabs recommends "
        f"{champion['model']} "
        f"for further evaluation."
    )

    print()
    print("=" * 80)