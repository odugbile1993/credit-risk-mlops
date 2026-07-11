"""
Input preprocessing utilities.

This module prepares borrower information
for model prediction.
"""

import pandas as pd


def prepare_input(
    revolving_utilization,
    age,
    past_due_30_59,
    debt_ratio,
    monthly_income,
    open_credit_lines,
    times_90_days_late,
    real_estate_loans,
    past_due_60_89,
    dependents,
):
    """
    Create a DataFrame in the exact format expected
    by the trained model.
    """

    return pd.DataFrame(
        {
            "RevolvingUtilizationOfUnsecuredLines": [revolving_utilization],
            "age": [age],
            "NumberOfTime30-59DaysPastDueNotWorse": [past_due_30_59],
            "DebtRatio": [debt_ratio],
            "MonthlyIncome": [monthly_income],
            "NumberOfOpenCreditLinesAndLoans": [open_credit_lines],
            "NumberOfTimes90DaysLate": [times_90_days_late],
            "NumberRealEstateLoansOrLines": [real_estate_loans],
            "NumberOfTime60-89DaysPastDueNotWorse": [past_due_60_89],
            "NumberOfDependents": [dependents],
        }
    )